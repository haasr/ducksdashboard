from admin_pages.models import SiteLook, UserProfile
from django.contrib.auth.models import User

x = SiteLook(
    id=1,
    navigation_img_size='width: 90%;',
)
x.save()

print('\n###### Create initial admin account ######')
print('You must create an initial admin account\nto log into <hostname>/users/login/\n')
fname = input('  First Name: ')
lname = input('  Last Name:  ')
mail  = input('  Email:      ')
uname = input('  Username:   ')
pswd  = input('  Password:   ')

new_usr = User.objects.create_user(first_name=fname, last_name=lname, email=mail,
                                    username=uname, password=pswd, is_staff=True)
new_usr.save()

usr_profile = UserProfile(
    #profile_img_name='profile-default.gif',
    user=new_usr
    role='Hacker'
)