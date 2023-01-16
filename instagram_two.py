#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install instabot


# In[2]:


from instabot import Bot


# In[4]:


my_bot = Bot()

#login into our Instagram account
my_bot.login(username="matteolai88", password="Silvio123!")

sleep(15)


#follow a user
my_bot.follow("python_app_projects")

sleep(15)


#follow multiple users
my_bot.follow_users(["coding_for_beginners", "py_beginners", "python.app"])

sleep(20)


#unfollow the non followers
my_bot.unfollow_non_followers()

sleep(15)


#upload an image
my_bot.upload_photo("kazimierz.jpg")
sleep(15)


#send message to user
my_bot.send_message("Ciao Magda, come stai?", "matteolai88")
sleep(20)


#like a post
try:
    my_bot.like_user("matteolai88", amount=2, filtration=False)
except Exception:
    print(Exception)

sleep(20)


#comment
try:
    user_id = my_bot.get_user_id_from_username("matteolai88")
    media_id = my_bot.get_last_user_medias(user_id, 1)
    my_bot.comment(media_id[0], "this is nice, I love it")
except Exception:
    print(Exception)



sleep(20)

#get list of followers of anyone
followers_list = my_bot.get_users_followers("drmaggiekrk")

following_list = my_bot.get_users_following("drmaggiekrk")

for count, each_follower in enumerate(followers_list):
    if count > 4:
        continue
    sleep(15)
    print(my_bot.get_username_from_user_id(each_follower))

for count1, each_follow in enumerate(following_list):
    if count > 4:
        continue
    sleep(15)
    print(my_bot.get_username_from_user_id(each_follow))
    
my_bot.logout()


# In[ ]:




