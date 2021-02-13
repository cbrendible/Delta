print('Welcome to Neverland Adventure!')
print('By Cymba')

# where to start
print('''
Wendy, John, and Michael are sleeping soundly in 
their beds when they hear a noise. Wendy gets up to 
inspect what the noise was while John gets out of 
bed and grabs his umbrella and holds it in front 
of him. Michael finds his teddy bear and gets up 
to hide behind his brother...
''')

player_pick = input('Choose your character... (Wendy/John/Michael) ')

if player_pick == 'Wendy':
    print('Great choice! You have chosen Wendy!')

    open_window = input('''
You hear the noises coming from the window... 
Do you open it? (yes/no) ''')

    if open_window == 'yes':
        print('''
Wendy approaches the window and opens it...

Finding nothing suspicious, Wendy turns back to 
her brothers. Their faces behold a look of 
fright...

Wendy asks,\"John, Michael, what is it?" 

John replies,\"I think it\'s a shadow, Wendy..." 

Wendy turns back to the window just in time to see 
a shadow dart through the air and head into a 
drawer in a nightstand...''')

        investigate_shadow = input('''
Wendy agrees with John... Do you investigate? (yes/no) ''')

        if investigate_shadow == 'yes':
            print('''
Wendy approaches where they saw the shadow hide... 
She opens the drawer very slowly to peak in, 
and it suddenly darts out! All three gasp 
in astonishment as the shadow soars around on 
the walls of the room...

Wendy tries to calm the shadow\'s frantic 
flitting about, but it\'s no use. Suddenly 
another shadow darts inside and grabs the 
one flying around... only... It\'s not a shadow; 
it\'s a boy! 

The boy is struggling to hold onto the 
mysterious shadow when he loses his grip, and the 
shadow slingshots into the shadow of a bedpost 
and is momentarily stunned, giving the boy a 
chance to pin the shadow down... 

The siblings watch as the boy tries to 
attach the shadow to himself with various 
different items and with each item, the boy 
gets more frusterated that nothing is working...''')

            shadows_owner = input('''
Will Wendy offer her assistance to the distraught boy? (yes/no) ''')

            if shadows_owner == 'yes':
                print('''
Wendy grabs a needle and thread to sew the
boy\'s shadow back on... When Wendy 
approaches the boy, she asks, \"Would 
you like some help, boy?"

The boy, covered in patches of dirt, nods 
his head... 

Wendy tells the boy that it may hurt a 
little and begins sewing. The silence starts 
to get to Wendy...''')

                the_boys_name = input('''
Does she ask for the boy\'s name? (yes/no) ''')

                if the_boys_name == 'yes':
                    print('''
As Wendy finishes up mending the boy\'s shadow, 
she asks, \"What\'s your name?" 

The boy looks at her curiously before standing 
up like a proud eagle, fists on hips, and 
replying, \"My name\'s Peter! Peter Pan!" 

Wendy grins and holds out her hand for a 
handshake while saying, \"It\'s a pleasure to 
meet you, Peter Pan; I\'m Wendy Darling." 

Peter Pan looks at Wendy\'s hand in confusion t
hen looks up at Wendy... Wendy explains, \"You 
shake it. It\'s a form of greeting." 

Peter grabs Wendy\'s fingers and shakes it back 
and forth.''')

                    go_on_an_adventure = input('''
Peter Pan asks, \"Would you like to go on an adventure, 
Wendy Darling?"... (yes/no) ''')

                    if go_on_an_adventure == 'yes':
                        print('''
Peter Pan jumps into the air and starts flying 
around the nursery...

The boys are in awe, and Wendy can only gape in 
astonishment. Michael pipes up, \"I wanna fly too!" 

Peter Pan stops his flight around the nursery 
and looks at all 3 of his new friends... 
\"You must have happy thoughts to fly," he 
says seriously.''')
                    else:
                        print('')

                else:
                    print('Wendy continues in silence while the boy looks on in confusion... GAME OVER!')
            else:
                print('The boy grabs his shadow and leaves... GAME OVER!')
        else:
            print('Wendy nudges John to inspect the mysterious shadow...')
    else:
        print('Must have just been hearing things... GAME OVER')

elif player_pick == 'John':
    print('Good choice! You have chosen John!')
    print('You urge Wendy to open the window...')
else:
    print('Good choice! You have chosen Michael!')
