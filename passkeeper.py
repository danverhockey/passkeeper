import tkinter as tk
import sqlite3

def clear_entry(entry_name):
    entry_name.delete(0, 'end')

def show_all_entries():
    connection = sqlite3.connect("passbook.db")
    cursor = connection.cursor()
    rows = cursor.execute("SELECT Company, Username, Password FROM passwords").fetchall()

    all_entries = ""
    for entry in sorted(rows):
        all_entries = all_entries + f"{entry[0]}, Username: {entry[1]}, Password: {entry[2]}\n"

    show_all_result["text"] = all_entries

    cursor.close()
    connection.close()

def show_single_entry():
    company = single_entry.get().lower()
    connection = sqlite3.connect("passbook.db")
    cursor = connection.cursor()
    rows = cursor.execute("SELECT Company, Username, Password FROM passwords").fetchall()

    match = False
    for entry in rows:
        if entry[0] == company:
            match = True
            single_entry_result["text"] = f"Company: {entry[0]}, Username: {entry[1]}, Password: {entry[2]}"
    if not match:
        single_entry_result["text"] = "Company Doesn't Exist"

    cursor.close()
    connection.close()

    clear_entry(single_entry)

def add_entry():
    company = add_entry_company_entry.get().lower()
    username = add_entry_username_entry.get()
    password = add_entry_password_entry.get()

    connection = sqlite3.connect("passbook.db")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO passwords VALUES ('{company}', '{username}', '{password}')")
    connection.commit()

    cursor.close()
    connection.close()

    clear_entry(add_entry_company_entry)
    clear_entry(add_entry_username_entry)
    clear_entry(add_entry_password_entry)

def update_password():
    company = update_entry_company_entry.get().lower()
    password = update_entry_password_entry.get()

    connection = sqlite3.connect("passbook.db")
    cursor = connection.cursor()
    cursor.execute(f"UPDATE passwords SET Password = '{password}' WHERE company = '{company}'")
    connection.commit()

    cursor.close()
    connection.close()

    clear_entry(update_entry_company_entry)
    clear_entry(update_entry_password_entry)

def delete_entry():
    company = delete_entry_entry.get().lower()

    connection = sqlite3.connect("passbook.db")
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM passwords WHERE company = '{company}'")
    connection.commit()

    cursor.close()
    connection.close()

    clear_entry(delete_entry_entry)

window = tk.Tk()
window.title("Pass Keeper")
window.resizable(width=True, height=True)

window.columnconfigure([0, 1, 2], weight=1, minsize=300)
window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], weight=1, minsize=35)

# Show all entries
show_all_button = tk.Button(text="Show All Entries", command=show_all_entries)
show_all_result = tk.Label()
show_all_button.grid(row=0, column=0)
show_all_result.grid(row=0, column=1)

# Show single entry
single_entry_label = tk.Label(text="Show single entry, enter in company name: ")
single_entry = tk.Entry()
single_entry_button = tk.Button(text="Submit", command=show_single_entry)
single_entry_result = tk.Label()
single_entry_label.grid(row=1, column=0)
single_entry.grid(row=2, column=0)
single_entry_button.grid(row=3, column=0)
single_entry_result.grid(row=2, column=1)

# Add entry
add_entry_label = tk.Label(text="Add Entry")
add_entry_company_label = tk.Label(text="Enter in company name: ")
add_entry_company_entry = tk.Entry()
add_entry_username_label = tk.Label(text="Enter in username: ")
add_entry_username_entry = tk.Entry()
add_entry_password_label = tk.Label(text="Enter in password: ")
add_entry_password_entry = tk.Entry()
add_entry_button = tk.Button(text="Submit", command=add_entry)

add_entry_label.grid(row=4, column=1)
add_entry_company_label.grid(row=5, column=0)
add_entry_company_entry.grid(row=6, column=0)
add_entry_username_label.grid(row=5, column=1)
add_entry_username_entry.grid(row=6, column=1)
add_entry_password_label.grid(row=5, column=2)
add_entry_password_entry.grid(row=6, column=2)
add_entry_button.grid(row=7, column=1)

# Update Password
update_entry_label=tk.Label(text="Update Entry")
update_entry_company_label = tk.Label(text="Enter in company name: ")
update_entry_company_entry = tk.Entry()
update_entry_password_label = tk.Label(text="Enter in new password: ")
update_entry_password_entry = tk.Entry()
update_entry_button = tk.Button(text="Submit", command=update_password)

update_entry_label.grid(row=8, column=1)
update_entry_company_label.grid(row=9, column=0)
update_entry_company_entry.grid(row=10, column=0)
update_entry_password_label.grid(row=9, column=1)
update_entry_password_entry.grid(row=10, column=1)
update_entry_button.grid(row=11, column=1)

# Delete Entry
delete_entry_label = tk.Label(text="Delete entry, enter in company name: ")
delete_entry_entry = tk.Entry()
delete_entry_button = tk.Button(text="Submit", command=delete_entry)

delete_entry_label.grid(row=12, column=1)
delete_entry_entry.grid(row=13, column=1)
delete_entry_button.grid(row=14, column=1)

window.mainloop()


