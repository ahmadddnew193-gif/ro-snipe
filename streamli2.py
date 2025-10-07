import streamlit as st
import requests
import time
import string
import random
import pandas as pd
session = requests.session()
ses2=requests.session()
itera = 0
available_user = []
def user_gen(length: any,number: bool,customuser=False,customusername="placeholder"):
        
        if customuser == False:
                if length < 3 :
                    raise ValueError
                if number == True:
                    chars= string.ascii_letters + string.digits
                    username_random = ''.join(random.choices(chars, k = length))
                    return username_random
                elif number == False:
                    chars = string.ascii_letters
                    username_random = ''.join(random.choices(chars,k=length))
                    return username_random
        else:
            custom_chars = string.ascii_letters
            customusername1= "".join(random.choices(custom_chars,k=len(customusername)//2+1))
            customusername3 = f"{customusername}{customusername1}"
            return customusername3


def checkuser(username: str,length,amount,custom: bool):
    global itera
    url = f"https://auth.roblox.com/v1/usernames/validate?Username={username}&Birthday=2000-01-01"

    resp = session.get(url=url)

    if not resp.status_code == 400:
        data = resp.json()
        if data["message"]=="Username is valid":
            st.success(f"Username is Available: {username} ,{itera+1}/{amount}" )
            if custom == False:
                 
                available_user.append(username)
            else:
                 custom_users.append(username)
            time.sleep(0.01)
            itera+=1


                
        else:
            print(f"Username Taken! >> {username}")



st.set_page_config(page_title="🎟Ro-User",layout="wide")

st.title("Roblox User Sniper")

custom_users = []
user_length = st.number_input("User Lenght",min_value=3,value=5)
amount_users = st.number_input("Amount of Users",min_value=1,value=1)
number_mode = st.number_input("Use Numbers",min_value=0,max_value=1,value=1)
custom_mode = st.number_input("Custom User Mode",min_value=0,max_value=1,value=0)
restart = st.button("Restart")
checkbox = st.checkbox("start sniping!")
holder = st.empty()
date = st.button("DataFrame")
numbers = None
randomuser=None
store_name = "e"
STOp = False

if restart:
     STOp = False


if checkbox:
        custom=True
        if number_mode == 0:
             numbers = False
        else:
             numbers = True
             
        custom_name="placeholder"
        if custom_mode == 1:
            custom=True
            custom_name=holder.text_input("Username",value="placeholder")
            custom_mode = 3
        if custom_name != "placeholder":
            store_name = custom_name
        if store_name != "e":
            while itera != amount_users:
                if custom == True:
                    print(amount_users)
                    try:
                        customuser=user_gen(5,numbers,True,customusername=store_name)
                        checkuser(customuser,67,amount_users,custom=True)
                    except Exception as e:
                
                
                        st.error(f"Error: {e}")
                
            customdf = pd.DataFrame({"Index": len(custom_users),
                                     "Names": custom_users})
            st.dataframe(customdf)
            STOp = True

            custom_name = "placeholder"
        if custom_mode == 0:
            custom = False
            while int(amount_users) != itera and STOp != True:
                try:
                    randomuser = user_gen(int(user_length),numbers,custom,store_name)
                    checkuser(randomuser,int(user_length),int(amount_users),custom=False)
                    if date:
                        df1 = pd.DataFrame({"Numbers": itera,
                                            "User": available_user})
                        if itera != amount_users:
                            chart = st.empty()
                            print(available_user)
                            chart.dataframe(df1)
                        elif itera == amount_users:
                             print("nice")

                except Exception as e:
                    st.error(f"Error: {e}") 
            chart.dataframe(available_user)
            STOp = True           
