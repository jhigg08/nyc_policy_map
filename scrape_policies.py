import requests
from bs4 import BeautifulSoup
import json
import re

main_url = "https://council.nyc.gov/districts/"
response = requests.get(main_url)
soup = BeautifulSoup(response.content, "html.parser")

district_cards = soup.select("a.district-card")
members = []

for card in district_cards:
    link = card.get("href")
    if not link.startswith("http"):
        link = f"https://council.nyc.gov{link}"

    name = card.select_one(".council-member-name")
    district_num = card.select_one(".council-member-district")

    if name and district_num:
        district_id = int(re.search(r"\d+", district_num.text.strip()).group())
        members.append({
            "district": district_id,
            "official": name.text.strip(),
            "link": link
        })

def get_policy_highlights(member_url):
    try:
        res = requests.get(member_url)
        member_soup = BeautifulSoup(res.content, "html.parser")

        # Try getting <p> tags and fallback to any text chunks
        paragraphs = member_soup.find_all("p")
        highlights = []

        for p in paragraphs:
            text = p.get_text().strip()
            if 40 < len(text) < 300:
                highlights.append(text)
            if len(highlights) >= 3:
                break

        return highlights
    except Exception as e:
        print(f"❌ Error reading {member_url}: {e}")
        return []


policy_data = []

for member in members:
    print(f"🔍 Scraping District {member['district']}: {member['official']}")
    policies = get_policy_highlights(member["link"])
    print(f"   → Found {len(policies)} policy items")
    policy_data.append({
        "district": member["district"],
        "official": member["official"],
        "term_start": "<<TBD>>",
        "policies": policies if policies else ["<<No policies found>>"]
    })

with open("policies.json", "w") as f:
    json.dump(policy_data, f, indent=2)

print("✅ Done. policies.json updated.")
