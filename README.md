# Home-Automation


When new technologies like voice control become available, the smart home industry is poised for explosive growth. It refers to the computerization of domestic activities. The thought behind this is to keep a remote climate. This will make life easier on a daily basis. We will be able to work more efficiently and save time thanks to this system. The proposed implementation of a smart home integrates lighting and ventilation under a single control, which can be fully controlled by voice commands and any smartphone application for Android or iOS. Using Google Voice, the home appliances can be controlled by voice. The primary benefit of this is that small devices can connect to the internet, making it simple to communicate, control, and manage them without human intervention.
In addition, it saves energy and provides a high level of security and safety. In this section, we will set up Google Help on the Raspberry Pi. This will be connected to an Android or smart phone that can take all voice commands and control the home appliances automatically.

task:
1. It is the device which is not only controlled by the Google Assistant but also can be controlled through IFTTT which is smart phone application.
2. It controls the On-Off status of light bulbs and fans in all 4 rooms of a single house, it is secured with Wi-Fi password known to house owners only.      This ensures it security.
3. Also for the further security, we connected the Google assistant to Gmail Account of house owner. Hence security procedures related to access Gmail        account are also included. So wherever his or her email address is connected to any smart phone that person is accessible to his home from anywhere in      the world.
4. This circuit will work only when following important three conditions are available.
   (1) Internet connection to both smart home and user smart phone.
   (2) Power supply to the smart devices in the home and enough charging to smart phone.
   (3) Voice command or IFTTT command given by user.
5. This circuit will enable 4 light bulbs.

Configure IFTTT:

• First step is creating account on IFTTT.
Note: Create account on IFTTT by using same e-mail id which you have used for Adafruit.
• After account creation, click on My Applets and then select New Applet shown below,
• After selecting a new applet, we get a new page in which we should click on to This is shown in the
below image.
• Then search for Google Assistant and select it.
• Now, enter voice phrases which we will use as a command for Google assistant.
We can enter any phrase as per our application. As you can see, the phrases entered in the above fields are
for making Light ON. For making Light OFF, we have to create another applet with different phrases.
• Now, we get another page on which we have to click on that option which is used to connect Google
Assistant with Adafruit.
• Then search for Adafruit and select it.
• After selecting Adafruit, choose action. Now enter what data we need to send to which feed of Adafruit
dashboard.
• Click on Create Action.

Read entire report about the project here: https://drive.google.com/file/d/1oUbzrXW5aKT3GdSjMdUW9zwqwH-CifQb/view
