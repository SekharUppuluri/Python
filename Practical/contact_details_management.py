# === Contact Details Management using Dictionary ===
print("===== Contact Details Management =====")
contact_details = {}

# Adding contact details
contact_details["Eren"] = "98450-11123"
contact_details["Mikasa"] = "98760-44221"
contact_details["Armin"] = "98987-55643"

print("\n----- Contacts after adding: -----")
print(contact_details)

# Updating a contact
contact_details["Mikasa"] = "99001-77654"
print("\n----- Contacts after updating Mikasa's number: -----")
print(contact_details)

# Deleting a contact
del contact_details["Armin"]
print("\n----- Contacts after deleting Armin: -----")
print(contact_details)

# Retrieving a specific contact
name = "Eren"
print(f"\nPhone number for {name}: {contact_details[name]}")

print("\n ----- End of Contact Details Management ----- // Developed by アニン。")