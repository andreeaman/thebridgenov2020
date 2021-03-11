## **Class Guide**

---------

=================================
### IMPORTANT
**DO NOT UPLOAD THE 'NO_SUBIR_COPYRIGHT_init_flask_consciencesai.zip' file OR ANY FILE INSIDE IT TO PUBLIC. IT HAS COPYRIGHT. USE ONLY WITH AWS-EC2 INSTANCE** 
=================================

**Work-in:**

1. Create AWS account
    - https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start
2. Generate putty key - Public & private  -- **Or from AWS directly**
    - https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

### Check city of the server (Ohio, London)!
On EC2:
3. Open Security Group - Inbound & Outbound all traffic. 
4. Key Pairs - Import keys - **Directly in AWS** 
5. Launch instance - Free tier -  Linux 2 AMI (HVM) SSD
    - With the key-pair
    - With the Security Group
    - All basics
    https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-launch-instance

6. Filezilla: ssh - To send files - https://filezilla-project.org/download.php
    - Connect using your private .ppk
    - Send 'consciencesai' folder inside 'NO_SUBIR_COPYRIGHT_init_flask_consciencesai.zip' file. 
    - The file you have to modify is named "main.py" that contains the flask server. 
    - If you use more more libraries, you will have to install it and test it. Good luck.

=================================
### IMPORTANT
**DO NOT UPLOAD THE 'NO_SUBIR_COPYRIGHT_init_flask_consciencesai.zip' file OR ANY FILE INSIDE IT TO PUBLIC. IT HAS COPYRIGHT. USE ONLY WITH AWS-EC2 INSTANCE** 
=================================

7. Connect to your EC2 instance and execute inside "consciencesai" folder:
    - sh ___EXECUTOR___yum.sh
    - Answer "y" to all questions.

Connect with Putty:
- https://docs.aws.amazon.com/es_es/AWSEC2/latest/UserGuide/putty.html

### Using a virtual machine:

- https://www.virtualbox.org/wiki/Downloads - VirtualBox
- https://ubuntu.com/download/desktop - Ubuntu
- https://www.microsoft.com/es-es/software-download/windows10 - Windows10

* Windows, Linux and Mac are tools to do a specific work* 

**FUNNY FACT: The code you have in delopment may not work in production!!!**

---------

**Work-out:**

8. Modify the "main.py" from flask folder in AWS with something different to test it.
9. other exercises
---------

*Remember, you have many cheatsheets. Learn to use it.*

*PythonTutor is your friend... take care of it.*

*Use Google everytime you need. Google must be your shadow.*

---------

**Lead Instructor**: *Gabriel Vázquez Torres*

- gabriel@thebridgeschool.es

*Tutorials*: https://calendly.com/gabrielvazqueztb

**Teacher Assistant**: *Clara Piniella Martinez*

- clara.piniella@thebridgeschool.es

*Tutorials*: https://calendly.com/clapiniella

**Teacher Assistant**: *Diomedes Barbero Martinez*

- diomedes@thebridgeschool.es

*Tutorials*: https://calendly.com/diomedes