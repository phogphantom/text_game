#INF360 -  Programming in Python
#Thomas Standley
#Mid-term project
#The Great Adventure, just a stand in title 



import random
import time
import textwrap

#This is figuring out how users might answer
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes", "Yes", "YES"]
no = ["N", "n", "no", "No", "NO"]

health = 10 #This is the starting amount of health for the player.


#This starts defing the varibles
storyInter = 'Coming from deep inside your mind you hear a strange voice. Speaking sweet and soft a woman\'s voice says: "Wake up, death is not ready for you"...'

storyIntro = 'You slowly open your eyes and all you see is a blinding bright light. You try and raise your arm to block it out but the pain is incredible. You slowly turn onto you side and as soon as you move there is a searing sharp pain that runs through the back of your skull. You use your other arm and touch the back of your head, finding it crusted in dried blood. Now laying on your side you open your eyes again and see that the light is coming from a small hole a long ways above you and everything else is covered in darkness. As your eyes adjust more you can tell the walls are rock and you could probably crawl to the nearest one. While deciding what to do a sudden great fear comes over you. You have no idea where you are and how you ended up here. Do you:'

storyCrawlA = 'You slowly crawl while reaching out with your hands to the wall nearest you. Every movement brings unbearable pain. After a few short moments you finally feel the rock surface. As you reach up you find a small ledge that you can grab on to. After some struggle you finally manage to pull yourself to your feet. Looking behind you, you can see the small pinhole of light shining down into a massive cavern. Do you:'

storyCrawlB = 'Slowly you turn your body away from the wall nearest you. With every movement, more agonizing than the last, you crawl for what seems like an eternity. While panting hard, you reach your hand out to pull you along one more time and you feel nothing. You quickly realize the ground is no longer beneath your hands. You can\'t see anything but you reach your hands down and can feel that the rock edge goes straight down. You realize this must be a large crevice in the ground. Do you:'

storyStand = 'With excruciating pain you roll from your side onto your stomach. You take a few deep breaths to rest for a moment and let some of the blinding pain subside. Slowly you pull your knees under you and sit up. You put one foot in front of you and then push up. Screaming, you stand and slowly bring both feet under you. Instantly you feel dizzy and fall. You don\'t even feel your head smash the ground.'

storyWallRight = 'You leave your hand on the wall and turn to your right. You are walking very cautiously in complete darkness with an unbelievable amount of pain. Without warning you run head first into a wall. Making the pain blind you for a moment. Do you:'

storyWallLeft = 'You place your right hand on the wall and slowly turn your body around. Cautiously you follow the wall for several steps. Your steps are slow because of the pain. To your left you pass where the light is hitting the floor to the cavern. You stop to take a breath. Do you:'

storyWallTurnAround = 'After taking a few moments to regain your thoughts you slowly turn your self back around. You follow the wall while keeping your hand up to make sure you don\'t run into anything. You pass the spot you first stood at and keep walking. To your left you pass where the light is hitting the floor to the cavern. You stop to take a breath. Do you:'


storyWallLight = 'Breathing hard you are looking at where the light is hitting the cavern floor. Slowly pushing yourself off the wall you take one step, then another. You stand for a moment to catch your balance. With extreme difficulty you put one foot in front of the other, almost falling a few times. Panting you reach the light. Slowly you put your hand in the light, it feels warm. Then you walk fully into the light. You feel your feet leave the ground. Floating you hear the same voice as before: “You are not yet ready”. You then slam back to the ground.'

storyWallFollow = 'With your hand on the wall you keep walking. The wall slowly curves towards you. After a few more steps you can see that the wall ends. You take another step and notice you are standing the mouth of a tunnel. The light is directly behind you. Do you:'

storyStandLight = 'Breathing hard you are looking at where the light is hitting the cavern floor. You stand for a moment to catch your balance. With extreme difficulty you put one foot in front of the other, almost falling a few times. Panting you reach the light. Slowly you put your hand in the light, it feels warm. Then you put your whole body. You feel your feet leave the ground. Floating you hear the same voice as before: “You are not yet ready”. You then slam back to the ground.'

walkStright_question_story = 'You slowly pull yourself back to your feet. Looking sright ahead you can see the out line of what looks like an opening to a tunnel or smaller cave. Do you walk stright ahead? (Y/N)'

walkStright_question_story_no = 'You stand there for a few moments to gather your thoughts. You feel the light pull you back in. Once again your feet are off the ground. The voice comes back: "Again young one you are not read." You slammed to the ground again.'

storyCreviceRight = 'With an extreme effort you back away from the crevice to keep from falling in. With your hands you find the edge. Using your hands to pull yourself to your right you start crawling. Almost immediately your hand hits what feels like a root hanging from the celing. Grasping it with both hands you pull yourself to your feet. Panting, you stand there for a moment to catch your breath. Your eyes have adjusted enough that you can see the edge of the crevice. You also see the light coming through the ceiling and hitting the floor.'
 
storyCreviceLeft = 'Backing up slowly you turn your body. Your eyes are adjusting and you see a few feet in front of you. It looks like there is a large object in front of you so you start crawling towards it. After only a few moments of painful crawling that object you saw becomes clear. It is a wall that has a sort of rope ladder on it. You pull yourself up to your feet screaming the entire time. Do you crawl up the ladder?(Y/N)'

storyCreviceLeftLadder = 'You try to climb up the ladder slowly. You hear a snap and the ladder swings over the crevice. You hang on with all your strength but the other rope on the ladder snaps. You are flung into the crevice. There is nothing for you to grab onto and you are falling into the darkness. As the bottom rushes up you fade out.'

storyCreviceDown = 'Peering over the edge your eyes are adjusting enough that you can see the walls of the crevice. You can’t see the bottom or how deep it is but you the walls of the crevice look like it can be scaled. You slowly swing your legs around and dangle your body over the edge. You find some foot holds and start to move slowly down. Stopping to catch your breath you feel the wall crumble under your feet. The entire wall breaks apart plunging you into the depths. You don’t even feel your body smash into the crevice floor.'

storyFallCrevice = 'After regaining your balance you put your hand back on the wall. You take a few steps before your stomach jumps into your throat. The earth is going up wards as you are falling in the dark abyss. The bottom rushes up to meet you, but you never feel it.'

storyCreviceRightFollow = 'After standing for a few moments you notice that you can see the edge of the crevice. You keep walking and the wall turns slightly towards you. ou take another step and notice you are standing the mouth of a tunnel. The light is directly behind you. Do you:'

storyWalkStright = 'You stand in the mouth of the tunnel for a few moments. Finally your eyes are adjusting and some features are becoming clear. There is a small statue in the center against the wall. On either side of the statue is openings for two differnt tunnels. As you get close the statue starts to glow through its cracks.'

storyTouchStatue = 'The statue looks like a young woman with long robe on holding an owl in her left hand and a sword in the other. Her eyes are covered with a cloth. As you reach your hand out the staue starts glowing brighter. You place your hand on top. A power rushes through you and you see flashes of a giant battle that only last a moment. You step back reeling, but you are not in as much pain as before. Do you:'

storyTunnelRight = 'You look both directions and it looks like both tunnels are the same in size. You turn twords the tunnel on the right and start walking. Entering the tunnel you see the walls are covered in torches, lighting your path. After some time the tunnel comes in an abrut end antoher statue that looks exactly like the first one. That same voice comes back:"If you take the Holy Light will you use it to empower yourself?(Y/N) '  

storyTunnelLeft = 'Looking at both tunnels you take a step towards the tunnel on your left. Instantly you see the statue start glowing a deep red. The tunnel is in complete darkness. Slowly taking a few steps an incredible bright light shines a few feet in front of you. You feel the light peirce your body. A shrill voice screams: "You are not worthy of the Holy Light!"'

storySword = 'In your right hand you see a beam of light. When the light fades you are holding a blade. The sword looks like it was forged for a God. A sapphire glows with power in the pommel and an owl is engraved on the hilt. You can feel the power rushing through your body. You look forward and all you see is a bright light.'

storySelfEmpower = 'The familar voice screams: "You are incredibly selfish. The Holy Light could be used to change the future and end these horrible times! You are not worthy of the Light"'

storyEmpowerPeopleNo = 'In a stern tone you hear the familiar voice: "You don\'t want to empower yourself but yet you won\'t empower the people. A hero must do all things for the benefit of the people. You are not yet ready for the light"'

storyEnd = 'That soft familiar voice comes back: "You are the hero that the world needs. I know you have many questions and they will be answered in time. For now know that the fate of all life is dependant on how you use the Holy Light. Go forth and don\'t let the darkness take ahold in your heart."'

required = ('Use only A, B, or C. Not case sesitive')
required_2 = ('Answer yes or no')

#The following are to allow all the varibles to wrap. 
wrapper = textwrap.TextWrapper(width=75)
interWrap = wrapper.fill(text=storyInter)
introWrap = wrapper.fill(text=storyIntro)
crawlA_wrap = wrapper.fill(text=storyCrawlA)
crawlB_wrap = wrapper.fill(text=storyCrawlB)
stand_wrap = wrapper.fill(text=storyStand)
wallRight_wrap = wrapper.fill(text=storyWallRight)
wallLeft_wrap = wrapper.fill(text=storyWallLeft)
wallLight_wrap = wrapper.fill(text=storyWallLight)
creviceRight_wrap = wrapper.fill(text=storyCreviceRight)
creviceLeft_wrap = wrapper.fill(text=storyCreviceLeft)
creviceDown_wrap = wrapper.fill(text=storyCreviceDown)
standLight_wrap = wrapper.fill(text=storyStandLight)
walkStright_question_wrap = wrapper.fill(text=walkStright_question_story)
walkStright_question_no_wrap = wrapper.fill(text=walkStright_question_story_no)
fallCrevice_wrap = wrapper.fill(text=storyFallCrevice)
wallTurnAround = wrapper.fill(text=storyWallTurnAround)
wallFollow_wrap = wrapper.fill(text=storyWallFollow)
creviceLeftLadder_wrap = wrapper.fill(text=storyCreviceLeftLadder)
creviceRightFollow_wrap = wrapper.fill(text=storyCreviceRightFollow)
walkStright_wrap = wrapper.fill(text=storyWalkStright)
touchStatue_wrap = wrapper.fill(text=storyTouchStatue)
tunnelRight_wrap = wrapper.fill(text=storyTunnelRight)
tunnelLeft_wrap = wrapper.fill(text=storyTunnelLeft)
sword_wrap = wrapper.fill(text=storySword)
selfEmpower_wrap = wrapper.fill(text=storySelfEmpower)
empowerPeopleNo_wrap = wrapper.fill(text=storyEmpowerPeopleNo)
end_wrap = wrapper.fill(text=storyEnd)


while health > 0 and sword == 0:
	def addHealth(): #Done, adds health to palyer may not use
		global health
		health += random.randint(1,10)
	def loseHealth(): #Done, subtracts health to player, 'taking damage'
		global health
		health -= random.randint(1,10)
	def instaDeath(): #Done, causes instant death. 
		global health
		health = 0

	def interlude(): #This is the start. If the player dies and wats to play again it will start here.
		print('#' *50)
		print(interWrap)
		print('#' *50)
		time.sleep(.25)
		print('')
		global health
		health = 10
		choice = input('Wake up?(Y/N)')
		if choice in yes:
			intro()
		elif choice in no:
			print('We will be waiting')
		else:
			print(required_2)
			interlude()


	def intro(): 
		print('')
		print('#' *50)
		print(introWrap)
		time.sleep(.25)
		print('')
		print('Current health:' + str(int(health)))
		print('')
		print('''
A. Crawl to the wall and try to stand
B. Crawl in the opposite direction
C. Try to stand where you are''')
		choice = input('>>> ') #This will the first choice by the player.
		if choice in answer_A:
			crawl_A()
		elif choice in answer_B:
			crawl_B()
		elif choice in answer_C:
			stand()
		else:
			print(required)
			intro()

	def crawl_A(): #Crawls to wall to stand
		print('')
		print('#' *50)
		time.sleep(.15)
		print(crawlA_wrap)
		time.sleep(.25)
		print('')
		print('Current health:' + str(int(health)))
		print('')
		print('''
A. Follow the wall to the right
B. Follow the wall to the left
C. Try to walk towards the light''')
		choice = input('>>>')
		if choice in answer_A:
			wallRight()
		elif choice in answer_B:
			wallLeft()
		elif choice in answer_C:
			wallLight()

	def crawl_B(): #Crawls and finds crevice
		print('')
		print('#' *50)
		time.sleep(.15)
		print(crawlB_wrap)
		time.sleep(.25)
		print('')
		print('Current health:' + str(int(health)))
		print('')
		print('''
A. Follow the crevice to your right.
B. Follow the crevice to your left.
C. Try to climb down the crevice.''')
		choice = input('>>>')
		if choice in answer_A:
			creviceRight()
		elif choice in answer_B:
			creviceLeft()
		elif choice in answer_C:
			creviceDown()

	def stand(): #stands where the player is
		print('')
		print('#' *50)
		time.sleep(.15)
		print(stand_wrap)
		time.sleep(1)
		print('')
		print('')
		print('')
		loseHealth()
		print('')
		print('')
		print('Current health:' + str(int(health)))
		if health > 0:
			print('''
A. Crawl to the wall.
B. Try to stand again and walk towards the light.''')
			choice = input('>>>')
			if choice in answer_A:
				crawl_A()
			if choice in answer_B:
				standLight() 

	def wallRight(): #goes right on the wall
		print('')
		print('#' *50)
		time.sleep(.15)
		print(wallRight_wrap)
		time.sleep(.25)
		print('')
		loseHealth()
		print('')
		print('Current health:' + str(int(health)))
		print('')
		print('''
A. Turn around
B. Walk away from the wall''')
		if health > 0:
			choice = input('>>>')
			if choice in answer_A:
				wallTurn()
			elif choice in answer_B:
				print(fallCrevice_wrap) 
				instaDeath()
				time.sleep(2)
				print('''
				
				
				''')
				

	def wallLeft(): #goes left on the wall
		print('')
		print('#' *50)
		time.sleep(.15)
		print(wallLeft_wrap)
		print('')
		print('Current health:' + str(int(health)))
		time.sleep(.25)
		print('')
		print('''
A. Keep following the wall
B. Walk to the light''')
		choice = input('>>>')
		if choice in answer_A:
			wallFollow()
		if choice in answer_B:
			wallLight()

	def wallLight(): #walks to light after standing
		print('')
		print('#' *50)
		time.sleep(.15)
		print(wallLight_wrap)
		time.sleep(.25)
		loseHealth()
		print('')
		print('')
		print('Current health:' + str(int(health)))
		print('')
		if health > 0: 
			print(walkStright_question_wrap)
			choice = input('>>>')
			if choice in yes:
				walkStright()
			if choice in no:
				print(walkStright_question_no_wrap)
				instaDeath()
				time.sleep(2)
				print('''
				
				
				''')
			
		
	def wallTurn(): #turns around after hitting head
		print('')
		print('#' *50)
		print(wallTurnAround)
		time.sleep(.25)
		print('')
		print('')
		print('Current health:' + str(int(health)))
		print('')
		print('''
A. Keep following the wall
B. Walk to the light''')
		choice = input('>>>')
		if choice in answer_A:
			wallFollow()
		if choice in answer_B:
			wallLight()
	
	def wallFollow(): #keepings following wall, ends in first tunnel
		print('')
		print('#' *50)
		print(wallFollow_wrap)
		time.sleep(.25)
		print('')
		print('')
		print('Current health:' + str(int(health)))
		print('')
		print('''
A. Walk stright into the tunnel
B. Walk towards the light
		''')
		choice = input('>>>')
		if choice in answer_A:
			walkStright()
		if choice in answer_B:
			wallLight()
	
	def creviceRight(): #stands after finding root
		print('')
		print('#' *50)
		time.sleep(.15)
		print(creviceRight_wrap)
		print('')
		print('Current health:' + str(int(health)))
		print('')
		print('''
A. Keep following the crevice
B. Walk towards the light''')
		choice = input('>>>')
		if choice in answer_A:
			creviceRightFollow()
		if chice in answer_B:
			standLight()

	def creviceRightFollow(): #ends in first tunnel
		print('')
		print('#' *50)
		time.sleep(.15)
		print(creviceRightFollow_wrap)
		print('')
		print('''
A. Walk sright
B. Walk to the light''')
		choice = input('>>>')
		if choice in answer_A:
			walkStright()
		if choice in answer_B:
			standLight()
	
	def creviceLeft(): #player finds ladder, falls to death
		print('')
		print('#' *50)
		time.sleep(.15)
		print(creviceLeft_wrap)
		time.sleep(.25)
		print('')
		print('Current health:' + str(int(health)))
		print('')
		choice = input('>>>')
		if choice in yes:
			print(creviceLeftLadder_wrap)
			instaDeath()
			time.sleep(5)
			print('''
			
			
			''')
		
			
				
	def creviceDown(): #try to climb down crevice, causes death
		print('')
		print('#' *50)
		time.sleep(.15)
		print(creviceDown_wrap)
		instaDeath()
		time.sleep(5)
		print('''
		
		
		''')
		
		
	def walkStright(): #walks into tunnel 
		print('')
		print('#' *50)
		print(walkStright_wrap)
		time.sleep(.15)
		print('')
		print('Current health:' + str(int(health)))
		print('')
		print('Touch the statue?(Y/N)')
		choice = input('>>>')
		if choice in yes:
			print(touchStatue_wrap)
			addHealth()
			print('')
			print('Current health:' + str(int(health)))
			print('')
			print('')
			print('''
A. Go in the tunnel on your right
B. Go in the tunnel on your left''')
			choice = input('>>>')
			if choice in answer_A:
				tunnelRight()
			if choice in answer_B:
				tunnelLeft()
		if choice in no:
			print('''
A. Go in the tunnel on your right
B. Go in the tunnel on your left''')
			choice = input('>>>')
			if choice in answer_A:
				tunnelRight()
			if choice in answer_B:
				tunnelLeft()

	def tunnelRight(): #This is the tunnel that is the endgame, player will finish if answering the questions correctly. 
		print('')
		print('#' *50)
		print(tunnelRight_wrap)
		time.sleep(.15)
		choice = input('>>>')
		if choice in yes:
			print('')
			print(selfEmpower_wrap)
			print('''
			
			
			''')
			time.sleep(3)
			instaDeath()
			
		if choice in no:
			print('Will you use the Holy Light is empower the people?(Y/N)')
			choice = input('>>>')
			if choice in yes:
				print(sword_wrap)
				time.sleep(3)
				end()
			if choice in no:
				print('')
				print(empowerPeopleNo_wrap)
				print('''
			
			
				''')
				time.sleep(3)
				instaDeath()
				
			
	def tunnelLeft(): #goes down left tunnel, causes death
		print('')
		print('#' *50)
		print(tunnelLeft_wrap)
		instaDeath()
		print('''
		
		
		''')
		time.sleep(3)
		
	def standLight(): #walk into light, take damage. 
		print('')
		print('#' *50)
		print(standLight_wrap)
		time.sleep(.15)
		print('')
		loseHealth()
		print('')
		print('Current health:' + str(int(health)))
		print('')
		if health > 0: 
			print(walkStright_question_wrap)
			choice = input('>>>')
			if choice in yes:
				walkStright()
			if choice in no:
				print(walkStright_question_no_wrap)
				instaDeath()
				time.sleep(2)
				print('''
				
				
				''')
		if health < 0:
			print('')
				
	def creviceDown(): #Falls down crevice, causes death
		print('')
		print('#' *50)
		print(creviceDown_wrap)
		instaDeath()
		time.sleep(4)
		print('''
		
		
		''')
		
	def end(): #This is the end of the current game. Sets up what might be to come
		print('')
		print('#' *50)
		print('')
		print(end_wrap)
		time.sleep(3)
		print('''
		
		
		''')
		input('Go forth')
			
	interlude()
else: #This asks the player to play again
	print('')
	choice = input('Death is trying to pull you in. Keep fighting back?(Y/N)')
	if choice in yes:
		interlude()
	if choice in no:
		input('Enter to exit')
		


	
	
	



