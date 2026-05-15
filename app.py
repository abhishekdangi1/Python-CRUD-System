import streamlit as st
from pathlib import Path
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Python CRUD Project", layout="centered")
st.title("🐍 Python CRUD Operations")

# --- FUNCTIONS (Slightly modified for Streamlit) ---

def readfileandfolder():
    p = Path('.')
    # Hum hidden files (.git, .devcontainer) ko list nahi karenge
    items = [str(file) for file in p.rglob('*') if not str(file).startswith('.')]
    return items

# --- SIDEBAR MENU (Replaces your 'while True' loop) ---
st.sidebar.header("Navigation")
option = st.sidebar.radio("Kya karna chahte hain?", 
    ["View Files", "Create File", "Read File", "Update File", "Delete File", "Rename File", "Create Folder", "Delete Folder"])

# --- MAIN LOGIC ---

if option == "View Files":
    st.subheader("Current Files & Folders")
    items = readfileandfolder()
    if items:
        for item in items:
            st.text(f"📍 {item}")
    else:
        st.write("Koi file nahi mili.")

elif option == "Create File":
    st.subheader("1. Create a New File")
    file_name = st.text_input("Enter name of your file (e.g. data.txt):")
    content = st.text_area("Enter your file content:")
    if st.button("Create"):
        p = Path(file_name)
        if p.exists():
            st.error("FILE ALREADY EXISTS")
        else:
            with open(file_name, 'w') as file:
                file.write(content)
            st.success("FILE ADDED!")

elif option == "Read File":
    st.subheader("2. Read a File")
    file_name = st.text_input("Enter name of your file to read:")
    if st.button("Read"):
        p = Path(file_name)
        if p.exists() and p.is_file():
            with open(file_name, 'r') as file:
                st.code(file.read())
        else:
            st.error("FILE NOT FOUND!")

elif option == "Update File":
    st.subheader("3. Update a File")
    file_name = st.text_input("Enter name of file to update:")
    p = Path(file_name)
    if p.exists() and p.is_file():
        update_choice = st.selectbox("Kaise update karna hai?", ["Overwrite (Pura badle)", "Append (Niche jode)"])
        new_content = st.text_area("Enter new content:")
        if st.button("Update"):
            mode = 'w' if update_choice == "Overwrite (Pura badle)" else 'a'
            with open(file_name, mode) as file:
                file.write(new_content)
            st.success("CONTENT CHANGED...")
    else:
        st.info("Pehle sahi file name enter karein.")

elif option == "Delete File":
    st.subheader("4. Delete a File")
    file_name = st.text_input("Enter name of file to delete:")
    if st.button("Delete", type="primary"):
        p = Path(file_name)
        if p.exists() and p.is_file():
            os.remove(p)
            st.success("FILE DELETED")
        else:
            st.error("FILE DOES NOT EXISTS!!")

elif option == "Rename File":
    st.subheader("5. Rename File/Folder")
    file_name = st.text_input("Purana naam:")
    new_name = st.text_input("Naya naam:")
    if st.button("Rename"):
        p = Path(file_name)
        if p.exists():
            p.rename(new_name)
            st.success("RENAMED!")
        else:
            st.error("FILE NOT FOUND!")

elif option == "Create Folder":
    st.subheader("6. Create Folder")
    folder_name = st.text_input("Enter name of folder:")
    if st.button("Create Folder"):
        p = Path(folder_name)
        if p.exists():
            st.error("FOLDER ALREADY EXISTS!")
        else:
            p.mkdir()
            st.success("FOLDER CREATED!")

elif option == "Delete Folder":
    st.subheader("7. Delete Folder")
    folder_name = st.text_input("Enter name of folder to delete:")
    if st.button("Delete Folder"):
        p = Path(folder_name)
        if p.exists() and p.is_dir():
            try:
                p.rmdir()
                st.success("FOLDER DELETED!")
            except:
                st.error("Folder khali nahi hai, isliye delete nahi ho sakta.")
        else:
            st.error("FOLDER NOT FOUND!")
