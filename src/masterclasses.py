
from dataclasses import dataclass
from enum import Enum, auto

class PracticeType(Enum):
    PLAYER = auto()
    COMMENTS = auto()
    MEDITATION = auto()
    PITCH_IDENTIFY_DRILL = auto()
    PITCH_NAMING_DRILL = auto()

@dataclass
class Practice:
    id: int
    title: str
    description: str
    max_hits: int
    practice_type: PracticeType 
    link: str
    text: str
    practice_batch: list

@dataclass
class Masterclass:
    id: int
    title: str
    description: str
    practices: list[Practice]
    max_hits: int
    practice_type: PracticeType 


masterclasses = {
  "title": "Apsolute Pitch Trainer",
  "description": "based on David Lucas Burge",
  "version": "v0.0.1",
  "masterclasses": [
    {
      "id": 0,
      "title": "Tests",
      "description": "This masterclass is for testing only. It does not exists in DLB colection.",
      "practices": [
        {
          "id": 0,
          "title": "Listen to masterclass",
          "description": "Audio book player. Here you will listen to David Lucas Burge audio book.",
          "maxHits": 1,
          "practiceType": "PLAYER",
          "link": "https://youtu.be/l4CBhHD2kOM"
        },
        {
          "id": 1,
          "title": "Comment",
          "description": "Comments on the masterclass.",
          "maxHits": 1,
          "practiceType": "COMMENTS",
          "text": "In this section i will put my comments on the audio masterclass. I hope this will help you grasp everything together and better organize yourself. More comments to come.\n[b]bold[i]bold italic[/i][/b][i]italic[/i]\n[u]Underline[/u]\n[s]Strike[/s]\n[code]print(\"test\")[/code]"
        },
        {
          "id": 2,
          "title": "Meditation",
          "description": "Example meditation. This practice will give you a tone to sing. Check if you got it right.",
          "maxHits": 20,
          "practiceType": "MEDITATION",
          "practiceBatch": [
            {"id": 0,"question": [["c'"]],"anwser": [["c'"]]},
            {"id": 1,"question": [["d'"]],"anwser": [["d'"]]},
            {"id": 2,"question": [["e'"]],"anwser": [["e'"]]}
          ]
        },
        {
          "id": 3,
          "title": "Pitch identify drill",
          "description": "Example pitch identify drill. This practice will play 2 white tones separated by 1. You should sing the lower one.",
          "maxHits": 20,
          "practiceType": "PITCH_IDENTIFY_DRILL",
          "practiceBatch": [
            {"id": 0,"question": [["c'","e'"]],"anwser": [["c'"]]},
            {"id": 1,"question": [["d'","f'"]],"anwser": [["d'"]]},
            {"id": 2,"question": [["e'","g'"]],"anwser": [["e'"]]},
            {"id": 3,"question": [["f'","a'"]],"anwser": [["f'"]]},
            {"id": 4,"question": [["g'","h'"]],"anwser": [["g'"]]},
            {"id": 5,"question": [["a'","c''"]],"anwser": [["a'"]]},
            {"id": 6,"question": [["h'","d''"]],"anwser": [["h'"]]},
            {"id": 7,"question": [["c''","e''"]],"anwser": [["c''"]]}
          ]
        },
        {
          "id": 4,
          "title": "Pitch naming drill",
          "description": "Example pitch naming drill. This practice will play a C major chord and than a black tone. You should name the black tone.",
          "maxHits": 20,
          "practiceType": "PITCH_NAMING_DRILL",
          "practiceBatch": [
            {"id": 0,"question": [["c'","e'","g'"],["cis'"]],"anwser": [["cis'"]]},
            {"id": 1,"question": [["c'","e'","g'"],["es'"]],"anwser": [["es'"]]},
            {"id": 2,"question": [["c'","e'","g'"],["fis'"]],"anwser": [["fis'"]]},
            {"id": 3,"question": [["c'","e'","g'"],["as'"]],"anwser": [["as'"]]},
            {"id": 4,"question": [["c'","e'","g'"],["b'"]],"anwser": [["b'"]]}
          ]
        }
      ]
    },
    {
      "id": 1,
      "title": "Masterclass 1",
      "description": "Performer can only preform as well as he can hear. A composer can only compose what he can think up.",
      "practices": [
        {
          "id": 0,
          "title": "Listen to masterclass",
          "description": "Audio book player. Here you will listen to David Lucas Burge audio book.",
          "maxHits": 1,
          "practiceType": "PLAYER",
          "link": "https://www.youtube.com/watch?v=ueRNJv24oTY"
        },
        {
          "id": 1,
          "title": "Comments",
          "description": "Comments on the masterclass.",
          "maxHits": 1,
          "practiceType": "COMMENTS",
          "text": "Perfect pitch sounds so long good until you take your pace to practice it. It's always hard to learn something new. It takes time and energy.\n\n[b]Keywords[/b]\nPerformer can only preform as well as he can hear. A composer can only compose what he can think up. And you can only think up what your ear can comprehend, what your ear can grasp. You can only appreciate and enjoy whatever your own perception and awareness allows you to enjoy. It is all dependent on your own musical awareness. Perfect pitch is the color in music (black and white TV example). Its a delicate perception which opens up the ear in all area of music. Its something which is already in our ear."
        }
      ]
    },
    {
      "id": 2,
      "title": "Masterclass 2",
      "description": "",
      "practices": [
        {
          "id": 0,
          "title": "Listen to masterclass",
          "description": "Audio book player. Here you will listen to David Lucas Burge audio book.",
          "maxHits": 1,
          "practiceType": "PLAYER",
          "link": "https://www.youtube.com/watch?v=l4CBhHD2kOM"
        },
        {
          "id": 1,
          "title": "Comments",
          "description": "Comments on the masterclass.",
          "maxHits": 1,
          "practiceType": "COMMENTS",
          "text": "I'm a Double bass player. Now I remembered that I couldn't decide on which instrument to practice the exercises. He says that you should be on your live, own instrument but on the other hand that people with no musical experience can both learn perfect pitch. I'm a [code]python[/code] programming hobbyist and I will try to write all the practices.\n\n[b]Keywords[/b]\nRelative and perfect pitch are both important.\nRelative pitch help us to say that the chord is [i]dominant:9[/i] and perfect pitch is helping us to hear that it is on tone [b]d[/b].\nAbsolute means non changing. [b]A[/b] has always the same sound. It is absolute.\n\n[b]Different levels:[/b]\n[ul]color awareness\ncolor discrimination (12 chromatic pitch colors) - quality of sound\n[/ul]\n\n[b]Exercise[/b]\no to your own instrument and have a listen, here for yourself that this color sounds do exist.\n"
        }
      ]
    },
    {
      "id": 3,
      "title": "Masterclass 3",
      "description": "",
      "practices": [
        {
          "id": 0,
          "title": "Listen to masterclass",
          "description": "Audio book player. Here you will listen to David Lucas Burge audio book.",
          "maxHits": 1,
          "practiceType": "PLAYER",
          "link": "https://www.youtube.com/watch?v=ycBcUX6jcRk"
        },
        {
          "id": 1,
          "title": "Comments",
          "description": "Comments on the masterclass.",
          "maxHits": 1,
          "practiceType": "COMMENTS",
          "text": "About the tones. I didn't hear color as he said but I started to hear tones in space. I'm aware now that each tone has its own place in space.\n\np.s. don't force yourself.\n\n[b]Keywords[/b]\nWe learn to distinguish these colors between the very fine variations that there are the tones.\nBut they become very clear. We get to know this sound colors.\nWe have to get it out of that habit (listening horizontally) and into the habit of listening inside the tones.\nComposers have used variates keys and chords in different ways for different reasons even unconsciously.\nAbsolute pitch training is a effortless training. What we don't wanna do is practice perfect pitch training with this idea that your gonna get in there and force your ear and wipe it and shape. If you strain the ear will not hear. Ear will only feel when it feels comfortable and relaxed and you just let it listen.\nAs we do listen our color discrimination grows.\n\n3. level of perfect pitch: Refined color discrimination (you can tell if tone is sharp or flat to standard concert pitch)\n\nSome people think if you have perfect pitch that you have mental barometer in your brain witch just register [i]BOING[/i] and tells you exactly how high or low the pitch is.\n\nFirstly you can here this colors on your own instrument, but as soon as somebody plays it on some other instrument we have no idea, your completely lost. Now this is a common experience. This is perfect pitch but it's just one level of it. We can refine our hearing even more so that we can here it on all instruments. This would be called [b]Universal color discrimination[/b]. When the ear can here this colors clearly and recognized them in all the universal variety of pitches whether is our own instrument on piano, guitar, oboe, violin, bassoon, bells, little glasses of water, whistle or birds, voices.\nThe ear has to learn the distinction between pitch colors (pitch itself) and tone color (of the instrument). Spectral discrimination.\nIt's a human perception.\n\n4. level: aural recall (not raw memorising, it's hearing a color)\n\nWhen you want to sing Ab you don't judge how high or low the tone is. What you do you think up is the color sound. What does it sounds like.\n\n[b]Exercise[/b]\n[ul]Try F# ( 1 3 5 8 ) and Eb chords and listen to the difference. Were are not listening to a clear difference, it's a saddle thing. It's a feeling that when you play the F# chord and you move to the Eb something has changed.\nListen a little more for yourself.\nRead you perfect pitch handbook.\nAnother listen to the tones. Listen gently and easily to the tones.\n[/ul]"
        }
      ]
    },
    {
      "id": 4,
      "title": "Masterclass 4",
      "description": "",
      "practices": [
        {
          "id": 0,
          "title": "Listen to masterclass",
          "description": "Audio book player. Here you will listen to David Lucas Burge audio book.",
          "maxHits": 1,
          "practiceType": "PLAYER",
          "link": "https://www.youtube.com/watch?v=ZJhC8WnwpKk"
        },
        {
          "id": 1,
          "title": "Comments",
          "description": "Comments on the masterclass.",
          "maxHits": 1,
          "practiceType": "COMMENTS",
          "text": "[b]Q&A[/b]\nListen if your are interested.\n\n[b]Exercise[/b]\nBe creative and be a child for a while. Listen to all chromatic tones on your instrument. From c to c and try to find a color which best matches what you feel then draw it. Colored notes or rainbow. We don't wanna miss the start. Draw your own color chart.\n(Do the practice. It allows you to listen to the sounds creatively.)\n"
        }
      ]
    },
    {
      "id": 5,
      "title": "Masterclass 5",
      "description": "Just follow the method. Step by step.",
      "practices": [
        {
          "id": 0,
          "title": "Listen to masterclass",
          "description": "Audio book player. Here you will listen to David Lucas Burge audio book.",
          "maxHits": 1,
          "practiceType": "PLAYER",
          "link": "https://www.youtube.com/watch?v=yIICRXtdnac"
        },
        {
          "id": 1,
          "title": "Comments",
          "description": "Comments on the masterclass.",
          "maxHits": 1,
          "practiceType": "COMMENTS",
          "text": "[b]Keywords[/b]\n[ul][i]Phase 1[/i] - prep the ear\n[i]Phase 2[/i] - all the color become clear at the same time.\n[i]Phase 3[/i] - polish it even more[/ul]\n\nWere in a big class room.\nThe foundation on music is hearing.\nYou just follow the method. Step by step.\nWhen you do know how to listen and progress step by step it becomes simplified.\nYou need to take the time to listen. You can't rush it.\nListen to each session all the way through including the parts that may on may not apply to you.\n\nYou go to the next masterclass after you have successfully finished all exercises.\n\nWhat instrument to use.\nThe result will be faster if you use the instrument you play most. \nThe instrument that your ear is most familiar with.\nYou can use that training on any instrument. But you have to get used to the sound first.\nYou can't do chords on a flute. But you can have flute chords on synthesiser.\nUse that one sound for all your ear training practice all the way up until we get to phase 3.\nRelative pitch is a different story.\n\nWe wanna do about two octave bellow middle C and two octave above.\nStart up using a medium range of tones on your instrument at first.\n\nSome of the exercises that were going to do are hearing exercises and some are singing exercises.\nWhen your doing a hearing exercises you just listen, you don't sing the tone. We don't wanna start judging pitches with our voice. We wanna learn the pitch by hearing.\n\nWere going to divide our exercises into three main categories:\n\n[ol]solo keyboards\nsolo guitar\nteams of two (additional drill methods)[/ol]\n\nEar training meditation technique.\nIt is important to clearly understand the theory behind perfect pitch and how perfect pitch becomes cultured into the ear.\nWe want to listen to each masterclasse one at the time. We never wanna do more then one masterclass in a day.\nTake as long as you need to practice the exercises. Maybe you'll need even three weeks on one particular homework assignment from a masterclass.\nWe don't rush ourself. We go at our own pace.\nWe don't wanna be left behind on any step. This is a crucial secret to perfect pitch development.\nWe don't practice for a long time each day. The short ear training session is all it takes. Actually your ear will go faster if you just give it a short session but you do it daily.\n\nFor our solo practises we just wanna listen for about 10 or 15 minutes. Don't think you have to go on, and on, and on. Sometimes when people train their ear to much then they find they can't hear anything. Has this ever happen to you? It's like you can take a shower for 10 minutes or 30 minutes. But 10 minutes is plane.\n\nThe same for teams.\nProgress to the next masterclass when you feel ready. And if by chance you ever get stuck anywhere in your practice....\n\n[b]Exercise - Phase 1 - Color hearing:[/b]\n\n[b]Solo keyboards[/b]\nReach to your keyboard and play any two white tones that are separated by one white tone like E and G. Were just using the white tones only. Now we listen carefully to sound of these two tones. Listen individually so that you can hear each of the two tones. Usually we may only hear the top tone. So we have to listen little more closely to the bottom tone. Let your ear get inside to hear the bottom tone as well as the top tone. Now to prove that you really are hearing these tones we sing them (from the bottom up). When you can sing the tones then you have proved that you really have heard both tones. You didn't just hear the top one. If you can't hear the bottom tone than play it. Listen to it separately. Then play the two tones together again and see if you can now hear the bottom tone. Just work with your ear like this. Take your time. Work with this drill until you can any two tones separate by one white tone. You don't have to name the pitch. Were just singing the tones.\n\n[b]Solo guitar[/b]\nJust play a string at random and just try to tell which it is. Learn your string.\n\n[b]Solo instrumentalist[/b]\nEvan easter. Just listen carefully to C and D (regardless of your instrument, if your Bb instrument your C will sound Bb) and sing them very concisely like a meditation. Here is how we do it. Listen to C on your instrument. Gently hear the tone. Let it sock into your ear. Then here the pitch in your own mind. Imagine the pitch then sing the pitch (Laaa) and then sing the pitch again. Were just using C and D right now. We don't have to worry about any other tones. And were using it on our own instrument.\n\nHave fun!\n"
        },
        {
          "id": 2,
          "title": "Listen and sing",
          "description": "Any two white tones separated by one. Sing both tones from bottom to top.",
          "maxHits": 20,
          "practiceType": "PITCH_IDENTIFY_DRILL",
          "practiceBatch": [
            {"id": 0,"question": [["c,","e,"]],"anwser": [["c,","e,"]]},
            {"id": 1,"question": [["d,","f,"]],"anwser": [["d,","f,"]]},
            {"id": 2,"question": [["e,","g,"]],"anwser": [["e,","g,"]]},
            {"id": 3,"question": [["f,","a,"]],"anwser": [["f,","a,"]]},
            {"id": 4,"question": [["g,","h,"]],"anwser": [["g,","h,"]]},
            {"id": 5,"question": [["a,","c"]],"anwser": [["a,","c"]]},
            {"id": 6,"question": [["h,","d"]],"anwser": [["h,","d"]]},
            {"id": 7,"question": [["c","e"]],"anwser": [["c","e"]]},
            {"id": 8,"question": [["d","f"]],"anwser": [["d","f"]]},
            {"id": 9,"question": [["e","g"]],"anwser": [["e","g"]]},
            {"id": 10,"question": [["f","a"]],"anwser": [["f","a"]]},
            {"id": 11,"question": [["g","h"]],"anwser": [["g","h"]]},
            {"id": 12,"question": [["a","c'"]],"anwser": [["a","c'"]]},
            {"id": 13,"question": [["h","d'"]],"anwser": [["h","d'"]]},
            {"id": 14,"question": [["c'","e'"]],"anwser": [["c'","e'"]]},
            {"id": 15,"question": [["d'","f'"]],"anwser": [["d'","f'"]]},
            {"id": 16,"question": [["e'","g'"]],"anwser": [["e'","g'"]]},
            {"id": 17,"question": [["f'","a'"]],"anwser": [["f'","a'"]]},
            {"id": 18,"question": [["g'","h'"]],"anwser": [["g'","h'"]]},
            {"id": 19,"question": [["a'","c''"]],"anwser": [["a'","c''"]]},
            {"id": 20,"question": [["h'","d''"]],"anwser": [["h'","d''"]]},
            {"id": 21,"question": [["c''","e''"]],"anwser": [["c''","e''"]]},
            {"id": 22,"question": [["d''","f''"]],"anwser": [["d''","f''"]]},
            {"id": 23,"question": [["e''","g''"]],"anwser": [["e''","g''"]]},
            {"id": 24,"question": [["f''","a''"]],"anwser": [["f''","a''"]]},
            {"id": 25,"question": [["g''","h''"]],"anwser": [["g''","h''"]]},
            {"id": 26,"question": [["a''","c'''"]],"anwser": [["a''","c'''"]]}
          ]
        }
      ]
    },
    {
      "id": 6,
      "title": "Masterclass 6",
      "description": "The little experience of joy or happiness as an experience of the depth of perception which music has to offer.",
      "practices": [
        {
          "id": 0,
          "title": "Listen to masterclass",
          "description": "Audio book player. Here you will listen to David Lucas Burge audio book.",
          "maxHits": 1,
          "practiceType": "PLAYER",
          "link": "https://www.youtube.com/watch?v=Au0ns633Yps"
        },
        {
          "id": 1,
          "title": "Comments",
          "description": "Comments on the masterclass.",
          "maxHits": 1,
          "practiceType": "COMMENTS",
          "text": "[b]Keywords[/b]\nThe little experiance of joy or happynes as an experiance of the depth of perception which music has to offer.\n\n[b]Unlocking tehnique with major and minor secodns.[/b]\nWe go deeper into our color tehnique exercisses. Right now were getting our ear to zoom in on our tones to unlock them. So that were able to hear each tone discretly. Now were gana make it a little trickier. Were ganna do the same things with major and minor seconds.\n\n[i]Solo keyboards[/i]\n[ol]1. Major and minor seconds (harmonicly, only white tones). And were singing it from the bottom up (melodicly).\nA little bit of an ear teaser for you to sort out the top tone from the bottom tone. As you continue they clearify. When you can sing it then your ear has open up that much more.\n2. Unlock any two tones using one hand only (octave) and sing them from the bottom up.\n3. Unlock wide tones. This means we play our tones wide. We reach out with two hands and play tones that are more spaced out ( bigger then one octave ) and we sing them from the bottom up. The octave is not important. Were listening them in whatever the octave they are and were singing them in what ever range voice we can sing them\n[/ol]\n\n[i]Last unlocking solo drills.[/i]\n[ol]4. Do three tones close. Reach out play any three tones one handed. We listen , we unlock the sounds with our ears so we here each note discretly and then we sing them from the bottom up. And we check ourselfs.\n5. Three tones wide. Reach out, play two tones in one hand and one tone in the other hand.\n[/ol]\n\nRemember, go slow on this drills. We listen with great intrest. Remember, its the listening that is opening our ear. So evan if we can do this drill easily we still need to take time to listen. This is the key to development of perfect pitch. If you for example can't hear the middle tone in drill 4. Listen again, and play separatly. And then play the problem chord again. Allow you ear to relax. Don't strain or force you ear in any way. Any time you find that a chord is trickie it just go to proof that you ear was not hearing thise things all along. The ear was sleeping. It just shows we need ear traning. Keep working on our ear and youl find that it will cooperate and it will begin to hear this things. The magic formula is: keep listening, keep listening, keep listening and listen gently.\n\n[b]Meditation tehnique for this session[/b]\n[i]All instrumentalist[/i]\nWe play a tone, we think of it, and we sing it again.\nWe think the tone before we sing it. This is the diference.\nWe always correct our mistakes. We never just move on. We always take the time to hear the wrong note and the right note.\nDo it like a meditation. Slow, queit, easy and relaxed.\n\n[i]Solo guitar[/i]\nThe same as solo keyboards.\n\nWe'll considure to have pass that drill when we can do one verification round.\nA verification round means that you pass tweny examples in a row all corectly without a mistake.\nIf you didn't do it right you have to correct your error. If you make a mistake you have to go all over again. When you do one verification round then you have masterd this drill.\n15 minutes a day on the solo drills until your confortable with them.\n\n[i]Team drills[/i]\nMelodic and Harmonic pitch indentification. C and D exacept guitarist. Guitarist A and B(H).\n[ul]1. One person plays evan C or D and the other person names it. One verification round.\n2. Were ganna play two tones together. We indetify from the bottom up. Close or wide. When we play melodicly we always indentifie in the order that they were played.\n[/ul]\nDon't skip a drill if you think that they are easy.\n"
        },
        {
          "id": 2,
          "title": "SK seconds",
          "description": "Major and minor seconds (harmonicly, only white tones). And were singing it from the bottom up (melodicly). A little bit of an ear teaser for you to sort out the top tone from the bottom tone. As you continue they clearify. When you can sing it then your ear has open up that much more.",
          "maxHits": 20,
          "practiceType": "PITCH_IDENTIFY_DRILL",
          "practiceBatch": [
            {"id": 0,"question": [["c,","cis,"]],"anwser": [["c,","cis,"]]},
            {"id": 18,"question": [["cis,","a,"]],"anwser": [["cis,","a,"]]},
            {"id": 20,"question": [["cis,","h,"]],"anwser": [["cis,","h,"]]},
            {"id": 32,"question": [["d,","cis"]],"anwser": [["d,","cis"]]},
            {"id": 36,"question": [["es,","g,"]],"anwser": [["es,","g,"]]},
            {"id": 39,"question": [["es,","b,"]],"anwser": [["es,","b,"]]},
            {"id": 47,"question": [["e,","as,"]],"anwser": [["e,","as,"]]},
            {"id": 60,"question": [["f,","h,"]],"anwser": [["f,","h,"]]},
            {"id": 70,"question": [["fis,","h,"]],"anwser": [["fis,","h,"]]},
            {"id": 72,"question": [["fis,","cis"]],"anwser": [["fis,","cis"]]},
            {"id": 100,"question": [["a,","h,"]],"anwser": [["a,","h,"]]},
            {"id": 108,"question": [["a,","g"]],"anwser": [["a,","g"]]},
            {"id": 110,"question": [["b,","h,"]],"anwser": [["b,","h,"]]},
            {"id": 114,"question": [["b,","es"]],"anwser": [["b,","es"]]},
            {"id": 117,"question": [["b,","fis"]],"anwser": [["b,","fis"]]},
            {"id": 124,"question": [["h,","es"]],"anwser": [["h,","es"]]},
            {"id": 135,"question": [["c","e"]],"anwser": [["c","e"]]},
            {"id": 139,"question": [["c","as"]],"anwser": [["c","as"]]},
            {"id": 168,"question": [["es","g"]],"anwser": [["es","g"]]},
            {"id": 173,"question": [["es","c'"]],"anwser": [["es","c'"]]},
            {"id": 180,"question": [["e","a"]],"anwser": [["e","a"]]},
            {"id": 183,"question": [["e","c'"]],"anwser": [["e","c'"]]},
            {"id": 204,"question": [["fis","cis'"]],"anwser": [["fis","cis'"]]},
            {"id": 222,"question": [["as","h"]],"anwser": [["as","h"]]},
            {"id": 225,"question": [["as","d'"]],"anwser": [["as","d'"]]},
            {"id": 230,"question": [["as","g'"]],"anwser": [["as","g'"]]},
            {"id": 235,"question": [["a","d'"]],"anwser": [["a","d'"]]},
            {"id": 236,"question": [["a","es'"]],"anwser": [["a","es'"]]},
            {"id": 256,"question": [["h","es'"]],"anwser": [["h","es'"]]},
            {"id": 263,"question": [["h","b'"]],"anwser": [["h","b'"]]},
            {"id": 264,"question": [["c'","cis'"]],"anwser": [["c'","cis'"]]},
            {"id": 279,"question": [["cis'","fis'"]],"anwser": [["cis'","fis'"]]},
            {"id": 285,"question": [["cis'","c''"]],"anwser": [["cis'","c''"]]},
            {"id": 287,"question": [["d'","e'"]],"anwser": [["d'","e'"]]},
            {"id": 308,"question": [["e'","f'"]],"anwser": [["e'","f'"]]},
            {"id": 312,"question": [["e'","a'"]],"anwser": [["e'","a'"]]},
            {"id": 331,"question": [["fis'","as'"]],"anwser": [["fis'","as'"]]},
            {"id": 336,"question": [["fis'","cis''"]],"anwser": [["fis'","cis''"]]},
            {"id": 369,"question": [["a'","e''"]],"anwser": [["a'","e''"]]},
            {"id": 371,"question": [["a'","fis''"]],"anwser": [["a'","fis''"]]},
            {"id": 372,"question": [["a'","g''"]],"anwser": [["a'","g''"]]},
            {"id": 383,"question": [["b'","as''"]],"anwser": [["b'","as''"]]},
            {"id": 391,"question": [["h'","fis''"]],"anwser": [["h'","fis''"]]},
            {"id": 396,"question": [["c''","cis''"]],"anwser": [["c''","cis''"]]},
            {"id": 403,"question": [["c''","as''"]],"anwser": [["c''","as''"]]},
            {"id": 449,"question": [["f''","b''"]],"anwser": [["f''","b''"]]},
            {"id": 457,"question": [["fis''","c'''"]],"anwser": [["fis''","c'''"]]},
            {"id": 462,"question": [["g''","c'''"]],"anwser": [["g''","c'''"]]},
            {"id": 463,"question": [["as''","a''"]],"anwser": [["as''","a''"]]},
            {"id": 466,"question": [["as''","c'''"]],"anwser": [["as''","c'''"]]}
          ]
        },
        {
          "id": 4,
          "title": "SK unlock 2 wide",
          "description": "Unlock wide tones. This means we play our tones wide. We reach out with two hands and play tones that are more spaced out ( bigger then one octave ) and we sing them from the bottom up. The octave is not important. Were listening them in whatever the octave they are and were singing them in what ever range voice we can sing them.",
          "maxHits": 20,
          "practiceType": "PITCH_IDENTIFY_DRILL",
          "practiceBatch": [
            {"id": 19,"question": [["c,","as"]],"anwser": [["c,","as"]]},
            {"id": 43,"question": [["c,","as''"]],"anwser": [["c,","as''"]]},
            {"id": 67,"question": [["cis,","a"]],"anwser": [["cis,","a"]]},
            {"id": 70,"question": [["cis,","c'"]],"anwser": [["cis,","c'"]]},
            {"id": 80,"question": [["cis,","b'"]],"anwser": [["cis,","b'"]]},
            {"id": 103,"question": [["d,","h,"]],"anwser": [["d,","h,"]]},
            {"id": 163,"question": [["es,","d'"]],"anwser": [["es,","d'"]]},
            {"id": 205,"question": [["e,","c'"]],"anwser": [["e,","c'"]]},
            {"id": 226,"question": [["e,","a''"]],"anwser": [["e,","a''"]]},
            {"id": 238,"question": [["f,","d"]],"anwser": [["f,","d"]]},
            {"id": 263,"question": [["f,","es''"]],"anwser": [["f,","es''"]]},
            {"id": 287,"question": [["fis,","a"]],"anwser": [["fis,","a"]]},
            {"id": 301,"question": [["fis,","h'"]],"anwser": [["fis,","h'"]]},
            {"id": 314,"question": [["fis,","c'''"]],"anwser": [["fis,","c'''"]]},
            {"id": 379,"question": [["as,","as'"]],"anwser": [["as,","as'"]]},
            {"id": 389,"question": [["as,","fis''"]],"anwser": [["as,","fis''"]]},
            {"id": 409,"question": [["a,","h"]],"anwser": [["a,","h"]]},
            {"id": 425,"question": [["a,","es''"]],"anwser": [["a,","es''"]]},
            {"id": 445,"question": [["b,","a"]],"anwser": [["b,","a"]]},
            {"id": 457,"question": [["b,","a'"]],"anwser": [["b,","a'"]]},
            {"id": 470,"question": [["b,","b''"]],"anwser": [["b,","b''"]]},
            {"id": 509,"question": [["h,","c'''"]],"anwser": [["h,","c'''"]]},
            {"id": 518,"question": [["c","a"]],"anwser": [["c","a"]]},
            {"id": 526,"question": [["c","f'"]],"anwser": [["c","f'"]]},
            {"id": 534,"question": [["c","cis''"]],"anwser": [["c","cis''"]]},
            {"id": 538,"question": [["c","f''"]],"anwser": [["c","f''"]]},
            {"id": 555,"question": [["cis","h"]],"anwser": [["cis","h"]]},
            {"id": 573,"question": [["cis","f''"]],"anwser": [["cis","f''"]]},
            {"id": 601,"question": [["d","h'"]],"anwser": [["d","h'"]]},
            {"id": 634,"question": [["es","h'"]],"anwser": [["es","h'"]]},
            {"id": 645,"question": [["es","b''"]],"anwser": [["es","b''"]]},
            {"id": 656,"question": [["e","cis'"]],"anwser": [["e","cis'"]]},
            {"id": 674,"question": [["e","g''"]],"anwser": [["e","g''"]]},
            {"id": 743,"question": [["g","b"]],"anwser": [["g","b"]]},
            {"id": 744,"question": [["g","h"]],"anwser": [["g","h"]]},
            {"id": 765,"question": [["g","as''"]],"anwser": [["g","as''"]]},
            {"id": 770,"question": [["as","a"]],"anwser": [["as","a"]]},
            {"id": 816,"question": [["a","e''"]],"anwser": [["a","e''"]]},
            {"id": 849,"question": [["b","h''"]],"anwser": [["b","h''"]]},
            {"id": 865,"question": [["h","d''"]],"anwser": [["h","d''"]]},
            {"id": 905,"question": [["cis'","g'"]],"anwser": [["cis'","g'"]]},
            {"id": 909,"question": [["cis'","h'"]],"anwser": [["cis'","h'"]]},
            {"id": 911,"question": [["cis'","cis''"]],"anwser": [["cis'","cis''"]]},
            {"id": 1031,"question": [["g'","e''"]],"anwser": [["g'","e''"]]},
            {"id": 1049,"question": [["as'","fis''"]],"anwser": [["as'","fis''"]]},
            {"id": 1066,"question": [["a'","as''"]],"anwser": [["a'","as''"]]},
            {"id": 1091,"question": [["h'","fis''"]],"anwser": [["h'","fis''"]]},
            {"id": 1148,"question": [["f''","fis''"]],"anwser": [["f''","fis''"]]},
            {"id": 1159,"question": [["fis''","h''"]],"anwser": [["fis''","h''"]]},
            {"id": 1163,"question": [["g''","b''"]],"anwser": [["g''","b''"]]}
          ]
        },
        {
          "id": 5,
          "title": "SK unlock 3 close",
          "description": "Do three tones close. Reach out play any three tones one handed. We listen, we unlock the sounds with our ears so we here each note discretly and then we sing them from the bottom up. And we check ourselfs.",
          "maxHits": 20,
          "practiceType": "PITCH_IDENTIFY_DRILL",
          "practiceBatch": [
            {"id": 28,"question": [["c,","e,","fis,"]],"anwser": [["c,","e,","fis,"]]},
            {"id": 42,"question": [["c,","fis,","a,"]],"anwser": [["c,","fis,","a,"]]},
            {"id": 190,"question": [["es,","fis,","cis"]],"anwser": [["es,","fis,","cis"]]},
            {"id": 193,"question": [["es,","g,","a,"]],"anwser": [["es,","g,","a,"]]},
            {"id": 197,"question": [["es,","g,","cis"]],"anwser": [["es,","g,","cis"]]},
            {"id": 210,"question": [["es,","b,","h,"]],"anwser": [["es,","b,","h,"]]},
            {"id": 225,"question": [["e,","f,","h,"]],"anwser": [["e,","f,","h,"]]},
            {"id": 287,"question": [["f,","g,","b,"]],"anwser": [["f,","g,","b,"]]},
            {"id": 344,"question": [["fis,","as,","cis"]],"anwser": [["fis,","as,","cis"]]},
            {"id": 353,"question": [["fis,","a,","d"]],"anwser": [["fis,","a,","d"]]},
            {"id": 358,"question": [["fis,","b,","c"]],"anwser": [["fis,","b,","c"]]},
            {"id": 483,"question": [["as,","d","fis"]],"anwser": [["as,","d","fis"]]},
            {"id": 530,"question": [["a,","d","e"]],"anwser": [["a,","d","e"]]},
            {"id": 537,"question": [["a,","es","fis"]],"anwser": [["a,","es","fis"]]},
            {"id": 542,"question": [["a,","e","g"]],"anwser": [["a,","e","g"]]},
            {"id": 571,"question": [["b,","cis","e"]],"anwser": [["b,","cis","e"]]},
            {"id": 577,"question": [["b,","d","es"]],"anwser": [["b,","d","es"]]},
            {"id": 584,"question": [["b,","es","e"]],"anwser": [["b,","es","e"]]},
            {"id": 585,"question": [["b,","es","f"]],"anwser": [["b,","es","f"]]},
            {"id": 737,"question": [["cis","e","as"]],"anwser": [["cis","e","as"]]},
            {"id": 741,"question": [["cis","e","c'"]],"anwser": [["cis","e","c'"]]},
            {"id": 806,"question": [["d","g","b"]],"anwser": [["d","g","b"]]},
            {"id": 813,"question": [["d","as","c'"]],"anwser": [["d","as","c'"]]},
            {"id": 862,"question": [["es","as","c'"]],"anwser": [["es","as","c'"]]},
            {"id": 876,"question": [["es","h","d'"]],"anwser": [["es","h","d'"]]},
            {"id": 942,"question": [["f","fis","d'"]],"anwser": [["f","fis","d'"]]},
            {"id": 1137,"question": [["as","cis'","f'"]],"anwser": [["as","cis'","f'"]]},
            {"id": 1230,"question": [["b","cis'","es'"]],"anwser": [["b","cis'","es'"]]},
            {"id": 1283,"question": [["h","cis'","b'"]],"anwser": [["h","cis'","b'"]]},
            {"id": 1323,"question": [["c'","cis'","f'"]],"anwser": [["c'","cis'","f'"]]},
            {"id": 1392,"question": [["cis'","es'","h'"]],"anwser": [["cis'","es'","h'"]]},
            {"id": 1413,"question": [["cis'","fis'","h'"]],"anwser": [["cis'","fis'","h'"]]},
            {"id": 1608,"question": [["f'","g'","h'"]],"anwser": [["f'","g'","h'"]]},
            {"id": 1629,"question": [["f'","b'","h'"]],"anwser": [["f'","b'","h'"]]},
            {"id": 1705,"question": [["g'","as'","a'"]],"anwser": [["g'","as'","a'"]]},
            {"id": 1826,"question": [["a'","h'","cis''"]],"anwser": [["a'","h'","cis''"]]},
            {"id": 1829,"question": [["a'","h'","e''"]],"anwser": [["a'","h'","e''"]]},
            {"id": 1853,"question": [["a'","d''","g''"]],"anwser": [["a'","d''","g''"]]},
            {"id": 1897,"question": [["b'","d''","es''"]],"anwser": [["b'","d''","es''"]]},
            {"id": 1911,"question": [["b'","e''","fis''"]],"anwser": [["b'","e''","fis''"]]},
            {"id": 1944,"question": [["h'","d''","es''"]],"anwser": [["h'","d''","es''"]]},
            {"id": 1979,"question": [["h'","a''","b''"]],"anwser": [["h'","a''","b''"]]},
            {"id": 2034,"question": [["c''","b''","h''"]],"anwser": [["c''","b''","h''"]]},
            {"id": 2062,"question": [["cis''","f''","fis''"]],"anwser": [["cis''","f''","fis''"]]},
            {"id": 2081,"question": [["cis''","as''","b''"]],"anwser": [["cis''","as''","b''"]]},
            {"id": 2144,"question": [["es''","f''","g''"]],"anwser": [["es''","f''","g''"]]},
            {"id": 2161,"question": [["es''","as''","a''"]],"anwser": [["es''","as''","a''"]]},
            {"id": 2199,"question": [["f''","fis''","g''"]],"anwser": [["f''","fis''","g''"]]},
            {"id": 2231,"question": [["fis''","a''","c'''"]],"anwser": [["fis''","a''","c'''"]]},
            {"id": 2241,"question": [["g''","a''","c'''"]],"anwser": [["g''","a''","c'''"]]}
          ]
        },
        {
          "id": 6,
          "title": "SK unlock 3 wide",
          "description": "Three tones wide. Reach out, play two tones in one hand and one tone in the other hand.",
          "maxHits": 20,
          "practiceType": "PITCH_IDENTIFY_DRILL",
          "practiceBatch": [
            {"id": 764,"question": [["c,","a","c''"]],"anwser": [["c,","a","c''"]]},
            {"id": 1909,"question": [["cis,","c'","cis'"]],"anwser": [["cis,","c'","cis'"]]},
            {"id": 2276,"question": [["d,","e,","es'"]],"anwser": [["d,","e,","es'"]]},
            {"id": 2381,"question": [["d,","fis,","h''"]],"anwser": [["d,","fis,","h''"]]},
            {"id": 2665,"question": [["d,","d","g'"]],"anwser": [["d,","d","g'"]]},
            {"id": 3087,"question": [["d,","fis'","a''"]],"anwser": [["d,","fis'","a''"]]},
            {"id": 3298,"question": [["es,","f,","e"]],"anwser": [["es,","f,","e"]]},
            {"id": 3707,"question": [["es,","e","fis"]],"anwser": [["es,","e","fis"]]},
            {"id": 3756,"question": [["es,","f","c''"]],"anwser": [["es,","f","c''"]]},
            {"id": 4034,"question": [["es,","e'","es''"]],"anwser": [["es,","e'","es''"]]},
            {"id": 4293,"question": [["e,","fis,","h"]],"anwser": [["e,","fis,","h"]]},
            {"id": 4510,"question": [["e,","h,","a''"]],"anwser": [["e,","h,","a''"]]},
            {"id": 4700,"question": [["e,","f","b'"]],"anwser": [["e,","f","b'"]]},
            {"id": 4942,"question": [["e,","d'","fis''"]],"anwser": [["e,","d'","fis''"]]},
            {"id": 5220,"question": [["f,","fis,","h''"]],"anwser": [["f,","fis,","h''"]]},
            {"id": 5603,"question": [["f,","f","b'"]],"anwser": [["f,","f","b'"]]},
            {"id": 6491,"question": [["fis,","fis","g'"]],"anwser": [["fis,","fis","g'"]]},
            {"id": 6554,"question": [["fis,","as","cis''"]],"anwser": [["fis,","as","cis''"]]},
            {"id": 6946,"question": [["g,","as,","h,"]],"anwser": [["g,","as,","h,"]]},
            {"id": 6979,"question": [["g,","as,","as''"]],"anwser": [["g,","as,","as''"]]},
            {"id": 7157,"question": [["g,","cis","cis''"]],"anwser": [["g,","cis","cis''"]]},
            {"id": 7364,"question": [["g,","as","es'"]],"anwser": [["g,","as","es'"]]},
            {"id": 7698,"question": [["g,","cis''","d''"]],"anwser": [["g,","cis''","d''"]]},
            {"id": 8048,"question": [["as,","f","fis"]],"anwser": [["as,","f","fis"]]},
            {"id": 8118,"question": [["as,","g","f'"]],"anwser": [["as,","g","f'"]]},
            {"id": 8404,"question": [["as,","g'","a''"]],"anwser": [["as,","g'","a''"]]},
            {"id": 8422,"question": [["as,","as'","h''"]],"anwser": [["as,","as'","h''"]]},
            {"id": 8694,"question": [["a,","d","g"]],"anwser": [["a,","d","g"]]},
            {"id": 9609,"question": [["b,","as","c'''"]],"anwser": [["b,","as","c'''"]]},
            {"id": 9795,"question": [["b,","e'","b''"]],"anwser": [["b,","e'","b''"]]},
            {"id": 9914,"question": [["b,","c''","f''"]],"anwser": [["b,","c''","f''"]]},
            {"id": 10258,"question": [["h,","as","g'"]],"anwser": [["h,","as","g'"]]},
            {"id": 10357,"question": [["h,","c'","e'"]],"anwser": [["h,","c'","e'"]]},
            {"id": 10985,"question": [["c","c'","d'"]],"anwser": [["c","c'","d'"]]},
            {"id": 12214,"question": [["d","es'","a'"]],"anwser": [["d","es'","a'"]]},
            {"id": 12389,"question": [["d","d''","g''"]],"anwser": [["d","d''","g''"]]},
            {"id": 12625,"question": [["es","b","g'"]],"anwser": [["es","b","g'"]]},
            {"id": 12823,"question": [["es","g'","e''"]],"anwser": [["es","g'","e''"]]},
            {"id": 13070,"question": [["e","as","a'"]],"anwser": [["e","as","a'"]]},
            {"id": 13650,"question": [["f","c'","b''"]],"anwser": [["f","c'","b''"]]},
            {"id": 14261,"question": [["fis","b'","cis''"]],"anwser": [["fis","b'","cis''"]]},
            {"id": 14324,"question": [["fis","es''","a''"]],"anwser": [["fis","es''","a''"]]},
            {"id": 14379,"question": [["g","as","c''"]],"anwser": [["g","as","c''"]]},
            {"id": 14496,"question": [["g","cis'","e'"]],"anwser": [["g","cis'","e'"]]},
            {"id": 15862,"question": [["h","cis'","e''"]],"anwser": [["h","cis'","e''"]]},
            {"id": 16315,"question": [["c'","h'","fis''"]],"anwser": [["c'","h'","fis''"]]},
            {"id": 17067,"question": [["es'","f''","g''"]],"anwser": [["es'","f''","g''"]]},
            {"id": 17214,"question": [["e'","c''","a''"]],"anwser": [["e'","c''","a''"]]},
            {"id": 17428,"question": [["f'","f''","g''"]],"anwser": [["f'","f''","g''"]]},
            {"id": 18238,"question": [["cis''","fis''","g''"]],"anwser": [["cis''","fis''","g''"]]}
          ]
        }
      ]
    },
    {
      "id": 7,
      "title": "Masterclass 7",
      "description": "",
      "practices": [
        {
          "id": 0,
          "title": "Listen to masterclass",
          "description": "Audio book player. Here you will listen to David Lucas Burge audio book.",
          "maxHits": 1,
          "practiceType": "PLAYER",
          "link": "https://www.youtube.com/watch?v=ndN0EsreAqw"
        },
        {
          "id": 1,
          "title": "Comments",
          "description": "Comments on the masterclass.",
          "maxHits": 1,
          "practiceType": "COMMENTS",
          "text": "[b]Keywords[/b]\nYou with perfect pitch will be able to play far more better by ear then you without.\nExercise\n\n[i]Solo keyboard[/i]\n[ul]Reach out and play any white tone anywhere on the keyboard and name it. We're using the C major scale so you would know the tones by relative pitch. At this point we don't have full color discrimination. So the ear needs something to latch on to in order to know the tone. And thats fine if you know the tone by relative pitch. Just name the pitch. Don't be to hasty with your pitch naming. Go slowly. Listen to the tone. Take an interest in the tone. Allow a tone to soak for a moment. Something else is happening inside. If you get it wrong then pause. Listen to both tones. And you can even listen to it in a relationship to the C. One verification round.[/ul]\n\n[i]Solo guitars[/i]\nTwo stings at a time and unlock them by ear. From the bottom up. Reach out and play any two open strings and indentify them. Don't worry about finger knowlidge.\n\n[i]Meditation[/i]\n[ul]C, D and E. When ever we seat to practice we think of a C and sing it. We need to correct our error.[/ul]\n\n[i]Team players[/i]\nC, D and E. Harmonic and melodic pitch indentification.\n[ul]Single. Single tone pitch nameing drill.\nMelodic doubles.\nHarmonic doubles.[/ul]\n\nCorrect the error. This is where the ear traning comes in. We need to get listening benefit. We listen again to open more and more.\nSing a C and check. Sing a E. Take you timer and be very present in the moment. No verification round."
        },
        {
          "id": 2,
          "title": "Name any white tone",
          "description": "Reach out and play any white tone anywhere on the keyboard and name it. We're using the C major scale so you would know the tones by relative pitch.",
          "maxHits": 20,
          "practiceType": "PITCH_NAMING_DRILL",
          "practiceBatch": [
            {"id": 0,"question": [["c,"]],"anwser": [["c,"]]},
            {"id": 1,"question": [["cis,"]],"anwser": [["cis,"]]},
            {"id": 2,"question": [["d,"]],"anwser": [["d,"]]},
            {"id": 3,"question": [["es,"]],"anwser": [["es,"]]},
            {"id": 4,"question": [["e,"]],"anwser": [["e,"]]},
            {"id": 5,"question": [["f,"]],"anwser": [["f,"]]},
            {"id": 6,"question": [["fis,"]],"anwser": [["fis,"]]},
            {"id": 7,"question": [["g,"]],"anwser": [["g,"]]},
            {"id": 8,"question": [["as,"]],"anwser": [["as,"]]},
            {"id": 9,"question": [["a,"]],"anwser": [["a,"]]},
            {"id": 10,"question": [["b,"]],"anwser": [["b,"]]},
            {"id": 11,"question": [["h,"]],"anwser": [["h,"]]},
            {"id": 12,"question": [["c"]],"anwser": [["c"]]},
            {"id": 13,"question": [["cis"]],"anwser": [["cis"]]},
            {"id": 14,"question": [["d"]],"anwser": [["d"]]},
            {"id": 15,"question": [["es"]],"anwser": [["es"]]},
            {"id": 16,"question": [["e"]],"anwser": [["e"]]},
            {"id": 17,"question": [["f"]],"anwser": [["f"]]},
            {"id": 18,"question": [["fis"]],"anwser": [["fis"]]},
            {"id": 19,"question": [["g"]],"anwser": [["g"]]},
            {"id": 20,"question": [["as"]],"anwser": [["as"]]},
            {"id": 21,"question": [["a"]],"anwser": [["a"]]},
            {"id": 22,"question": [["b"]],"anwser": [["b"]]},
            {"id": 23,"question": [["h"]],"anwser": [["h"]]},
            {"id": 24,"question": [["c'"]],"anwser": [["c'"]]},
            {"id": 25,"question": [["cis'"]],"anwser": [["cis'"]]},
            {"id": 26,"question": [["d'"]],"anwser": [["d'"]]},
            {"id": 27,"question": [["es'"]],"anwser": [["es'"]]},
            {"id": 28,"question": [["e'"]],"anwser": [["e'"]]},
            {"id": 29,"question": [["f'"]],"anwser": [["f'"]]},
            {"id": 30,"question": [["fis'"]],"anwser": [["fis'"]]},
            {"id": 31,"question": [["g'"]],"anwser": [["g'"]]},
            {"id": 32,"question": [["as'"]],"anwser": [["as'"]]},
            {"id": 33,"question": [["a'"]],"anwser": [["a'"]]},
            {"id": 34,"question": [["b'"]],"anwser": [["b'"]]},
            {"id": 35,"question": [["h'"]],"anwser": [["h'"]]},
            {"id": 36,"question": [["c''"]],"anwser": [["c''"]]},
            {"id": 37,"question": [["cis''"]],"anwser": [["cis''"]]},
            {"id": 38,"question": [["d''"]],"anwser": [["d''"]]},
            {"id": 39,"question": [["es''"]],"anwser": [["es''"]]},
            {"id": 40,"question": [["e''"]],"anwser": [["e''"]]},
            {"id": 41,"question": [["f''"]],"anwser": [["f''"]]},
            {"id": 42,"question": [["fis''"]],"anwser": [["fis''"]]},
            {"id": 43,"question": [["g''"]],"anwser": [["g''"]]},
            {"id": 44,"question": [["as''"]],"anwser": [["as''"]]},
            {"id": 45,"question": [["a''"]],"anwser": [["a''"]]},
            {"id": 46,"question": [["b''"]],"anwser": [["b''"]]},
            {"id": 47,"question": [["h''"]],"anwser": [["h''"]]},
            {"id": 48,"question": [["c'''"]],"anwser": [["c'''"]]}
          ]
        },
        {
          "id": 3,
          "title": "C, D and E meditation",
          "description": "C, D and E. When ever we seat to practice we think of a C and sing it. We need to correct our error.",
          "maxHits": 20,
          "practiceType": "MEDITATION",
          "practiceBatch": [
            {"id": 0,"question": [["c,"]],"anwser": [["c,"]]},
            {"id": 1,"question": [["d,"]],"anwser": [["d,"]]},
            {"id": 2,"question": [["e,"]],"anwser": [["e,"]]},
            {"id": 3,"question": [["c"]],"anwser": [["c"]]},
            {"id": 4,"question": [["d"]],"anwser": [["d"]]},
            {"id": 5,"question": [["e"]],"anwser": [["e"]]},
            {"id": 6,"question": [["c'"]],"anwser": [["c'"]]},
            {"id": 7,"question": [["d'"]],"anwser": [["d'"]]},
            {"id": 8,"question": [["e'"]],"anwser": [["e'"]]},
            {"id": 9,"question": [["c''"]],"anwser": [["c''"]]},
            {"id": 10,"question": [["d''"]],"anwser": [["d''"]]},
            {"id": 11,"question": [["e''"]],"anwser": [["e''"]]},
            {"id": 12,"question": [["c'''"]],"anwser": [["c'''"]]}
          ]
        },
        {
          "id": 4,
          "title": "Melodic doubles",
          "description": "C D and E. Melodic pitch indentification. Melodic doubles.",
          "maxHits": 20,
          "practiceType": "PITCH_IDENTIFY_DRILL",
          "practiceBatch": [
            {"id": 0,"question": [["c,","d,"]],"anwser": [["c,","d,"]]},
            {"id": 2,"question": [["c,","c"]],"anwser": [["c,","c"]]},
            {"id": 3,"question": [["c,","d"]],"anwser": [["c,","d"]]},
            {"id": 4,"question": [["c,","e"]],"anwser": [["c,","e"]]},
            {"id": 6,"question": [["c,","d'"]],"anwser": [["c,","d'"]]},
            {"id": 7,"question": [["c,","e'"]],"anwser": [["c,","e'"]]},
            {"id": 8,"question": [["c,","c''"]],"anwser": [["c,","c''"]]},
            {"id": 9,"question": [["c,","d''"]],"anwser": [["c,","d''"]]},
            {"id": 10,"question": [["c,","e''"]],"anwser": [["c,","e''"]]},
            {"id": 11,"question": [["c,","c'''"]],"anwser": [["c,","c'''"]]},
            {"id": 13,"question": [["d,","c"]],"anwser": [["d,","c"]]},
            {"id": 14,"question": [["d,","d"]],"anwser": [["d,","d"]]},
            {"id": 15,"question": [["d,","e"]],"anwser": [["d,","e"]]},
            {"id": 16,"question": [["d,","c'"]],"anwser": [["d,","c'"]]},
            {"id": 18,"question": [["d,","e'"]],"anwser": [["d,","e'"]]},
            {"id": 19,"question": [["d,","c''"]],"anwser": [["d,","c''"]]},
            {"id": 20,"question": [["d,","d''"]],"anwser": [["d,","d''"]]},
            {"id": 21,"question": [["d,","e''"]],"anwser": [["d,","e''"]]},
            {"id": 23,"question": [["e,","c"]],"anwser": [["e,","c"]]},
            {"id": 24,"question": [["e,","d"]],"anwser": [["e,","d"]]},
            {"id": 25,"question": [["e,","e"]],"anwser": [["e,","e"]]},
            {"id": 30,"question": [["e,","d''"]],"anwser": [["e,","d''"]]},
            {"id": 31,"question": [["e,","e''"]],"anwser": [["e,","e''"]]},
            {"id": 34,"question": [["c","e"]],"anwser": [["c","e"]]},
            {"id": 36,"question": [["c","d'"]],"anwser": [["c","d'"]]},
            {"id": 38,"question": [["c","c''"]],"anwser": [["c","c''"]]},
            {"id": 41,"question": [["c","c'''"]],"anwser": [["c","c'''"]]},
            {"id": 43,"question": [["d","c'"]],"anwser": [["d","c'"]]},
            {"id": 44,"question": [["d","d'"]],"anwser": [["d","d'"]]},
            {"id": 46,"question": [["d","c''"]],"anwser": [["d","c''"]]},
            {"id": 47,"question": [["d","d''"]],"anwser": [["d","d''"]]},
            {"id": 48,"question": [["d","e''"]],"anwser": [["d","e''"]]},
            {"id": 51,"question": [["e","d'"]],"anwser": [["e","d'"]]},
            {"id": 53,"question": [["e","c''"]],"anwser": [["e","c''"]]},
            {"id": 55,"question": [["e","e''"]],"anwser": [["e","e''"]]},
            {"id": 57,"question": [["c'","d'"]],"anwser": [["c'","d'"]]},
            {"id": 59,"question": [["c'","c''"]],"anwser": [["c'","c''"]]},
            {"id": 60,"question": [["c'","d''"]],"anwser": [["c'","d''"]]},
            {"id": 62,"question": [["c'","c'''"]],"anwser": [["c'","c'''"]]},
            {"id": 63,"question": [["d'","e'"]],"anwser": [["d'","e'"]]},
            {"id": 66,"question": [["d'","e''"]],"anwser": [["d'","e''"]]},
            {"id": 67,"question": [["d'","c'''"]],"anwser": [["d'","c'''"]]},
            {"id": 68,"question": [["e'","c''"]],"anwser": [["e'","c''"]]},
            {"id": 69,"question": [["e'","d''"]],"anwser": [["e'","d''"]]},
            {"id": 70,"question": [["e'","e''"]],"anwser": [["e'","e''"]]},
            {"id": 72,"question": [["c''","d''"]],"anwser": [["c''","d''"]]},
            {"id": 73,"question": [["c''","e''"]],"anwser": [["c''","e''"]]},
            {"id": 74,"question": [["c''","c'''"]],"anwser": [["c''","c'''"]]},
            {"id": 75,"question": [["d''","e''"]],"anwser": [["d''","e''"]]},
            {"id": 76,"question": [["d''","c'''"]],"anwser": [["d''","c'''"]]}
          ]
        },
        {
          "id": 5,
          "title": "Harmonic doubles",
          "description": "C D and E. Harmonic pitch indentification. Harmonic doubles.",
          "maxHits": 20,
          "practiceType": "PITCH_IDENTIFY_DRILL",
          "practiceBatch": [
            {"id": 0,"question": [["c,"],["d,"]],"anwser": [["c,"],["d,"]]},
            {"id": 1,"question": [["c,"],["e,"]],"anwser": [["c,"],["e,"]]},
            {"id": 2,"question": [["c,"],["c"]],"anwser": [["c,"],["c"]]},
            {"id": 3,"question": [["c,"],["d"]],"anwser": [["c,"],["d"]]},
            {"id": 5,"question": [["c,"],["c'"]],"anwser": [["c,"],["c'"]]},
            {"id": 7,"question": [["c,"],["e'"]],"anwser": [["c,"],["e'"]]},
            {"id": 9,"question": [["c,"],["d''"]],"anwser": [["c,"],["d''"]]},
            {"id": 10,"question": [["c,"],["e''"]],"anwser": [["c,"],["e''"]]},
            {"id": 11,"question": [["c,"],["c'''"]],"anwser": [["c,"],["c'''"]]},
            {"id": 12,"question": [["d,"],["e,"]],"anwser": [["d,"],["e,"]]},
            {"id": 13,"question": [["d,"],["c"]],"anwser": [["d,"],["c"]]},
            {"id": 16,"question": [["d,"],["c'"]],"anwser": [["d,"],["c'"]]},
            {"id": 17,"question": [["d,"],["d'"]],"anwser": [["d,"],["d'"]]},
            {"id": 18,"question": [["d,"],["e'"]],"anwser": [["d,"],["e'"]]},
            {"id": 19,"question": [["d,"],["c''"]],"anwser": [["d,"],["c''"]]},
            {"id": 20,"question": [["d,"],["d''"]],"anwser": [["d,"],["d''"]]},
            {"id": 22,"question": [["d,"],["c'''"]],"anwser": [["d,"],["c'''"]]},
            {"id": 23,"question": [["e,"],["c"]],"anwser": [["e,"],["c"]]},
            {"id": 24,"question": [["e,"],["d"]],"anwser": [["e,"],["d"]]},
            {"id": 25,"question": [["e,"],["e"]],"anwser": [["e,"],["e"]]},
            {"id": 26,"question": [["e,"],["c'"]],"anwser": [["e,"],["c'"]]},
            {"id": 31,"question": [["e,"],["e''"]],"anwser": [["e,"],["e''"]]},
            {"id": 32,"question": [["e,"],["c'''"]],"anwser": [["e,"],["c'''"]]},
            {"id": 33,"question": [["c"],["d"]],"anwser": [["c"],["d"]]},
            {"id": 34,"question": [["c"],["e"]],"anwser": [["c"],["e"]]},
            {"id": 35,"question": [["c"],["c'"]],"anwser": [["c"],["c'"]]},
            {"id": 37,"question": [["c"],["e'"]],"anwser": [["c"],["e'"]]},
            {"id": 38,"question": [["c"],["c''"]],"anwser": [["c"],["c''"]]},
            {"id": 40,"question": [["c"],["e''"]],"anwser": [["c"],["e''"]]},
            {"id": 41,"question": [["c"],["c'''"]],"anwser": [["c"],["c'''"]]},
            {"id": 43,"question": [["d"],["c'"]],"anwser": [["d"],["c'"]]},
            {"id": 45,"question": [["d"],["e'"]],"anwser": [["d"],["e'"]]},
            {"id": 47,"question": [["d"],["d''"]],"anwser": [["d"],["d''"]]},
            {"id": 48,"question": [["d"],["e''"]],"anwser": [["d"],["e''"]]},
            {"id": 49,"question": [["d"],["c'''"]],"anwser": [["d"],["c'''"]]},
            {"id": 51,"question": [["e"],["d'"]],"anwser": [["e"],["d'"]]},
            {"id": 52,"question": [["e"],["e'"]],"anwser": [["e"],["e'"]]},
            {"id": 53,"question": [["e"],["c''"]],"anwser": [["e"],["c''"]]},
            {"id": 55,"question": [["e"],["e''"]],"anwser": [["e"],["e''"]]},
            {"id": 59,"question": [["c'"],["c''"]],"anwser": [["c'"],["c''"]]},
            {"id": 64,"question": [["d'"],["c''"]],"anwser": [["d'"],["c''"]]},
            {"id": 65,"question": [["d'"],["d''"]],"anwser": [["d'"],["d''"]]},
            {"id": 67,"question": [["d'"],["c'''"]],"anwser": [["d'"],["c'''"]]},
            {"id": 68,"question": [["e'"],["c''"]],"anwser": [["e'"],["c''"]]},
            {"id": 69,"question": [["e'"],["d''"]],"anwser": [["e'"],["d''"]]},
            {"id": 70,"question": [["e'"],["e''"]],"anwser": [["e'"],["e''"]]},
            {"id": 72,"question": [["c''"],["d''"]],"anwser": [["c''"],["d''"]]},
            {"id": 74,"question": [["c''"],["c'''"]],"anwser": [["c''"],["c'''"]]},
            {"id": 75,"question": [["d''"],["e''"]],"anwser": [["d''"],["e''"]]},
            {"id": 77,"question": [["e''"],["c'''"]],"anwser": [["e''"],["c'''"]]}
          ]
        }
      ]
    },
    {
      "id": 255,
      "title": "More",
      "description": "Here are some more options.",
      "practices": [
        {
          "id": 0,
          "title": "Settings",
          "maxHits": 1,
          "description": "Custom configuration.",
          "practiceType": "SETTINGS"
        },
        {
          "id": 1,
          "title": "Experiments",
          "maxHits": 1,
          "description": "Experimenting easy.",
          "practiceType": "EXPERIMENTS"
        }
      ]
    }
  ]
}
