import streamlit as st
import requests
import time
import string
import playaudio
import random
import pandas as pd

session = requests.session()
ses2 = requests.session()
itera = 0
available_user = []
custom_users = []

def user_gen(length: any, number: bool, customuser=False, customusername="placeholder"):
    if not customuser:
        if length < 3:
            raise ValueError
        chars = string.ascii_letters + string.digits if number else string.ascii_letters
        return ''.join(random.choices(chars, k=length))
    else:
        custom_chars = string.ascii_letters
        customusername1 = "".join(random.choices(custom_chars, k=len(customusername)//2 + 1))
        return f"{customusername}{customusername1}"

def checkuser(username: str, length, amount, custom: bool):
    global itera
    url = f"https://auth.roblox.com/v1/usernames/validate?Username={username}&Birthday=2000-01-01"
    resp = session.get(url=url)

    if resp.status_code != 400:
        data = resp.json()
        if data["message"] == "Username is valid":
            st.success(f"Username is Available: {username} ,{itera+1}/{amount}")
            if not custom:
                available_user.append(username)
            else:
                custom_users.append(username)
            time.sleep(0.01)
            itera += 1
        else:
            print(f"Username Taken! >> {username}")

st.set_page_config(page_title="🎟Ro-User", layout="wide")
st.title("Roblox User Sniper")

s1 = requests.session()
user_length = st.number_input("User Length", min_value=3, value=5)
amount_users = st.number_input("Amount of Users", min_value=1, value=1)
number_mode = st.number_input("Use Numbers", min_value=0, max_value=1, value=1)
custom_mode = st.number_input("Custom User Mode", min_value=0, max_value=1, value=0)
restart = st.button("Restart")
checkbox = st.checkbox("Start sniping!")
holder = st.empty()
date = st.button("DataFrame")
numbers = None
randomuser = None
store_name = "e"
STOp = False
count1 = 0

if st.checkbox("Amount of Users",key="AMOUNTT"):
    SURe = st.checkbox("U sure?")
    while SURe:

        try:
            response = s1.get(url=f"https://www.roblox.com/users/{count1}/profile")
            if response.status_code == 200:
                st.markdown("""
                <audio autoplay>
                <source src="https://raw.githubusercontent.com/ahmadddnew193-gif/ro-snipe/main/mi-bombo.mp3" type="audio/mpeg">
                </audio>
                """, unsafe_allow_html=True)
                st.success("✅ Roblox is online!")
                st.success(f"User Id: {count1}")
                count1 += 1
            else:
                st.info(f"User Id: {count1} may be terminated or banned")
        except Exception as e:
            st.error(e)

if st.checkbox("Check Roblox Status"):
    loop_status = st.checkbox("Loop Roblox Status")
    delay = st.slider("Loop delay (seconds)", min_value=2, max_value=30, value=5)

    while loop_status:
        try:
            status = requests.get("https://www.roblox.com", timeout=5)
            if status.status_code == 200:
                st.markdown("""
                <audio autoplay>
                <source src="https://raw.githubusercontent.com/ahmadddnew193-gif/ro-snipe/main/mi-bombo.mp3" type="audio/mpeg">
                </audio>
                """, unsafe_allow_html=True)
                st.success("✅ Roblox is online!")
            else:
                st.warning("⚠️ Roblox might be down.")
        except Exception as e:
            st.error(f"Error checking status: {e}")
        time.sleep(delay)

if restart:
    STOp = False

if checkbox:
    custom = True
    numbers = bool(number_mode)
    custom_name = "placeholder"

    if custom_mode == 1:
        custom = True
        custom_name = holder.text_input("Username", value="placeholder")
        custom_mode = 3

    if custom_name != "placeholder":
        store_name = custom_name

    if store_name != "e":
        while itera != amount_users:
            if custom:
                try:
                    customuser = user_gen(5, numbers, True, customusername=store_name)
                    checkuser(customuser, 67, amount_users, custom=True)
                except Exception as e:
                    st.error(f"Error: {e}")
        customdf = pd.DataFrame({"Index": list(range(len(custom_users))), "Names": custom_users})
        st.dataframe(customdf)
        STOp = True
        custom_name = "placeholder"

    if custom_mode == 0:
        custom = False
        while itera != amount_users and not STOp:
            try:
                randomuser = user_gen(user_length, numbers, custom, store_name)
                checkuser(randomuser, user_length, amount_users, custom=False)
                if date:
                    df1 = pd.DataFrame({"Numbers": list(range(itera)), "User": available_user})
                    if itera != amount_users:
                        chart = st.empty()
                        chart.dataframe(df1)
                    elif itera == amount_users:
                        print("nice")
            except Exception as e:
                st.error(f"Error: {e}")
        st.dataframe(available_user)
        STOp = True

