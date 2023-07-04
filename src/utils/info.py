"""
Information needed to create the graph of recycling stations

All information from:
https://www.wastereduction.gov.hk/en/community/crn_outlets.htm
https://www.mtr.com.hk/en/customer/services/system_map.html

"""

east_rail = ["Luen Wo Hui", "Tai Wai", "Fanling", "Lo Tak Court",
            "Tai Po Market", "Tai Wo", "Hung Hom"]
island = ["Sheung Wan", "Happy Valley", "Tin Hau", "Sai Ying Pun", "Quarry Bay",
            "Quarry Bay"]
kwun_tong = ["Yue Man Square", "San Po Kong"]
ma_on_shan = ["Shek Wu Hui"]
south_island = ["Ap Lei Chau", "Tin Wan"]
tseun_wan = ["Cheung Sha Wan", "Tai Kok Tsui", "Kwai Chung", "Jordan",
            "Sai Kung Town"]
tseung_kwan_o = ["Po Lam"]
tuen_ma = ["San Hui", "Walled City", "To Kwa Wan", "Yuen Long Hui", "Long Ping",
           "Kin Sang"]
tung_chung = ["Mui Wo", "Yi Pei Square"]

neighboring_lines = [("Quarry Bay", "Po Lam"), ("Sheung Wan", "Jordan"),
                     ("Sheung Wan","Ap Lei Chau"), ("Jordan", "Hung Hom"),
                     ("Jordan", "Yi Pei Square"), ("Jordan","San Po Kong"),
                     ("Tai Wai", "Shek Wu Hui"), ("To Kwa Wan", "Tai Wai")]

all_lines = [east_rail, island, kwun_tong, ma_on_shan, south_island, tseun_wan,
    tseung_kwan_o, tuen_ma, tung_chung]

all_stations = []
for line in all_lines:
    for station in line:
        all_stations.append(station)

addresses = {
    "Luen Wo Hui": "Shop 1, G/F, Grand Tower, No.15-23 Luen Wo Road,\nLuen Wo Market, Fanling",
    "Tai Wai": "Shop 1, G/F, Tin Po Building, 102-108 Chik Fuk Street,\nTai Wai, Shatin",
    "Fanling": "Shop A111, 1/F, Flora Plaza,\n88 Pak Wo Road, Fanling",
    "Lo Tak Court": "Shop 14, G/F, Cheong Wah Building,\n289-301 Castle Peak Road - Tsuen Wan, Tsuen Wan",
    "Tai Po Market": "G/F, Central Plaza, 51-59 Kwong Fuk Road, Tai Po",
    "Tai Wo": "",
    "Hung Hom": "Shop 1A & 1B, 83 Wuhu Street, Hung Hom",
    "Tai Wo": "Shop 13A, L1, Block C, Greenery Plaza,\n3 Chui Yi Street, Tai Po",
    "Sheung Wan": "G/F, Wing Hing Commercial Building,\n16 Sutherland Street, Sheung Wan",
    "Happy Valley": "Shop 3, G/F, Green Valley Mansion,\n51 Wong Nai Chung Road, Happy Valley",
    "Tin Hau": "Shop M & M1, G/F, Triumph Court,\n13-41 Electric Road, Tin Hau",
    "Tai Wo": "",
    "Sai Ying Pun": "G/F, 113 First Street, Sai Ying Pun",
    "Quarry Bay": "Shop 130 & 111, East Pavilion,\n1010-1056 King’s Road, Quarry Bay",
    "Kennedy Town:": "Shop 2, G/F, Lexington Hill,\n44B Belcher's St, Kennedy Town",
    "Yue Man Square": "Shop H, G/F, Kwan Sen Mansion,\n19-29 Mut Wah Street, Kwun Tong",
    "San Po Kong": "G/F, San Po Kong Mansion,\n98-100 Choi Hung Road, San Po Kong",
    "Shek Wu Hui": "G/F, 16 Lung Sum Avenue, Sheung Shui",
    "Ap Lei Chau": "Shop B & C, G/F, Happy View Building,\n165-167 Ap Lei Chau Main Street, Ap Lei Chau",
    "Tin Wan": "Shop 1 & 2, G/F, Shun Fung Court, \n15 Ka Wo Street, Aberdeen",
    "Cheung Sha Wan": "G/F, ONE NEW YORK, 468 Castle Peak Road,\nCheung Sha Wan",
    "Tai Kok Tsui": "Shop 1-3, G/F, Pak Sing Building,\n27-41 Tong Mi Road, Tai Kok Tsui",
    "Kwai Chung": "Shop 01 & 02, LG/F, Kwai Po Building,\n135-147 Shek Yam Road, Kwai Chung (Lei Muk Road Entrance)",
    "Jordan": "Shop 1-3, G/F, Wai Ching Court, 14-18 Wai Ching Street, Jordan",
    "Sai Kung Town": "G/F, 98 Man Nin Street, Sai Kung",
    "Po Lam": "Shop G19, G/F, MCP Central, 8 Yan King Road,\nPo Lam, Tseung Kwan O",
    "San Hui": "Shop 12, G/F, Ming Wai Building, 4-26 Tuen Mun Heung Sze Wui Road,\nSan Hui, Tuen Mun",
    "Walled City": "G/F & 1/F, 48 Lion Rock Road, Kowloon City",
    "To Kwa Wan": "Shop D, G/F, 93 Pau Chung Street,\nTo Kwa Wan (San Shan Road Entrance)",
    "Yuen Long Hui": "Shop 3-8, G/F, Far East Consortium Yuen Long Building,\n13-33 Yuen Long On Lok Road, Yuen Long",
    "Long Ping": "Shop K & L, G/F, Hung Fat House,\n87-99 Kau Yuk Road, Yuen Long",
    "Kin Sang": "Shop 3, G/F, Ori, 3 Leung Tak Street, Tuen Mun",
    "Mui Wo": "Shop D, G/F, Silver Centre Building,\n10 Mui Wo Ferry Pier Road, Mui Wo, Lantau",
    "Yi Pei Square": "G/F, 71 Ho Pui Street, Tsuen Wan",
}

operators = {
    "Luen Wo Hui": "Endeavour Environmental Education Foundation Limited",
    "Tai Wai": "Christian Family Service Centre",
    "Fanling": "North District Residents Association Limited",
    "Lo Tak Court": "The Boys’ Brigade, Hong Kong",
    "Tai Po Market": "Environmental Association Limited",
    "Hung Hom": "The Boys’ Brigade, Hong Kong",
    "Tai Wo": "Green Tai Po",
    "Sheung Wan": "Fong Chung Resources Management Co. Limited",
    "Happy Valley": "Green Council",
    "Tin Hau": "121C Society for Recycling",
    "Sai Ying Pun": "121C Society for Recycling",
    "Quarry Bay": "Buddhist Compassion Relief Tzu-Chi Foundation Hong Kong Limited",
    "Kennedy Town:": "ECO Foundation Limited",
    "Yue Man Square": "Christian Family Service Centre",
    "San Po Kong": "East Kowloon District Residents' Committee Limited",
    "Shek Wu Hui": "North District Residents Association Limited",
    "Ap Lei Chau": "Hong Kong Southern District Community Association Limited",
    "Tin Wan": "121C Society for Recycling",
    "Cheung Sha Wan": "Greeners Action",
    "Tai Kok Tsui": "Bonding Service Network Association Limited",
    "Kwai Chung": "The Boys’ Brigade, Hong Kong",
    "Jordan": "Yaumati Kai Fong Welfare Advancement Association Limited",
    "Sai Kung Town": "Sai Kung and Tseung Kwan O Women's Association Limited",
    "Po Lam": "Tseung Kwan O Kai Fong Joint Association Limited",
    "San Hui": "Green Opportunity Limited",
    "Walled City": "Christian Family Service Centre",
    "To Kwa Wan": "The Boys’ Brigade, Hong Kong",
    "Yuen Long Hui": "Green Alliances Limited",
    "Long Ping": "Pumen Foundation Limited",
    "Kin Sang": "New Territories West Power Eco Company",
    "Mui Wo": "OIWA Limited",
    "Yi Pei Square": "Association for Tsuen Wan Development",
}