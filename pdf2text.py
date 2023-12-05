from pdf2image import convert_from_path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import statistics
import fitz


doc = fitz.open('./sample_data/hai_lecture_slides.pdf') # open a document
slide_text = ""
for page in doc: # iterate the document pages
  slide_text += page.get_text() # get plain text encoded as UTF-8


def compute_cosine_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    similarity_score = cosine_sim[0][1]
    return similarity_score

chunks = ["So in this lecture we're going to still be quite general. I'm going to talk about natural language processing and I'm going to talk in the first part I'm going to talk about what it is and in the second part I am going to oh good point in a second part I am going to talk about to introduce the concept of an NLP pipeline which is something that we'll be dealing with in the lab a little bit tomorrow and then from next Friday onwards. So first a quick overview of natural English processing. This is a topic which is usually reserved for like graduate courses in themselves so we're only even scrape really the surface of it. First a quick warm-up question and just take a minute and think can someone give me a quick estimate of how many AIs are in this room? Anyone throws out a guess?", "I guess. Do you want individual phones or do you want like the types of hands? Well, that's the question, isn't it? Just as I have your best guess was your own assumption and tell me. Yeah. So can you speak? Yeah. So can you speak louder? Yes, sir. Yes, I'll say at least the amount of students' time to to support the health to still on the Okay. Yeah. Yeah. Yeah. Yeah. the amount of series. The amount of series and stuff on each. Oh, yeah. So we have like, you said 40, 50, 80, sorry. Okay, I think you have. 40, 50, 80, sorry. Okay, I think you have a low estimate of number in a room, but I get your point.", "Basically the number of students. You say a bit more than the number of students. Anybody else? Joe. Right. I mean you're getting to the point that I was trying to get at basically both of you which is that nowadays right most smartphones have actually quite a bit of embedded AI's inside them right and you mentioned Siri that's an excellent point but it's not the only thing. So if you have that one language engine which is like what you consider me Siri but that thing contains its own kind of subsystems to protest speech and then when you take a picture your camera has some AI inside it to correct pictures and then when you store that into your photo gallery app then there is some AI recognizing images right if you go into your photo app you can see like oh I want to search for cats and then he's gonna get you pictures of cats well the phone doesn't know what a cat is right there is some system specialized on that thing to deal with it. If you use things like Google translate then you also have a translation system in embedded in the AI.", "If you use something like Google Map or Apple Map, then there is a very complex route optimization AI inside it. So basically you can take hardware number of phones and computers and tablets they are and then multiply that by maybe five to ten different subsystems, always running and trying to basically get something for you and does not even counting the thing embedded into your smart watches or like smartly birds or whatever you have. And a certain number of these deal with language, right? You have a translation, special recognition, you have to some extent, image recognition deals with image with text as well, because if you want to search for cats you have to understand what a cat is so there is a step in there. And the reason for this is because language is at the key of interaction. When you interact between people, spoken of sign language or writing, when you interact with machines, I think that's common line interfaces, voice interfaces, interaction between machines, stuff like networking protocols are languages.", "They're formal languages, but they're still languages. The way you interact with your cats or your dog is also a form of a marriage. So language is really the key of how we interact with almost anything. And now, thanks to the recent advances in machine learning, deep learning and all that, we brought natural language back as a natural way of interacting with computers. So you wouldn't know that because you're all very young, but used to be that you couldn't speak to your phone. You had to type things. It was hard. But nowadays you can talk to it and most tasks can be automated that way. I want a precise one as a natural language that means languages which naturally evolved over time. So this is in contrast to something like PEPFON or C-plus which are not natural language. They're artificial and formal languages designed for specific purpose. The field of natural language processing tries to merge insights from many other fields.", "So at its core, you know, language, you can think that there's going to be some linguistics. And that is true to some extent, but it's a very shallow part of linguistics. Mostly it is things like computer science for the computational aspect of it. We want to automate things with the machine and AI for the autonomous aspect. We want to be able to extract insights from the text, we want to generate the text. We want the thing to be autonomous. There's two main self-filled in NFP, natural language understanding or NELU focuses more on finding insights and that would be the part we say, hey Siri, what time is it? And the natural language generation would be the part where Siri answers, it's 130. Is it 1.30? It's not 1.30, yes. So those are the two steps, but usually when we talk about NLP, most of the work is done on the understanding part because that is the hard part, so to speak.", "Okay. Natural language. Understanding focused on analyzing natural language. You might have noticed that we tend to generate a lot of data and a lot of it is text. So this stats were from two years ago. We haven't changed it yet, but I'm assuming they can only go higher, right? Five hundred million tweets sent each day, the size of English Wikipedia is 5 terabytes and something. And as humans we are obsessive hoarders of data, we store store everything we keep it nose may combat any later which is true it is handy you can actually get a lot of insights from that text data you can figure out how people feel about a movie or a product, a thing called sentiment. You can figure out what people are talking about, what are the topics which are in the main public discourse. You can figure out how to translate sentences without having to have someone who speak both languages going and then translate in my way.", "You can figure out how to make people vote for the candidate you want, the goal of propaganda and which is also using natural language understanding. And it's so much more. It is a rich field, it's used in many places, and we'll talk about that in the coming weeks. Natural language generis and systems, on the other hand, focus on generating that language. So you might have heard things called chatpots, right? Now, every time you go on the website, there is this very annoying pop-up on the bottom right he says, hey can I help you? I'm the chatbot for whatever store. You want to buy something? That's part of it, but there are other part of it when you, I don't know, I think the NHS has chatbots as well, or some counseling websites have chatbots. It's everywhere. You can also generate text from structural data to two main ones of financial reporting and weather prediction.", "So there are a lot in a lot of newspapers websites, there's a lot of small news items about the stock market, for instance, which are actually written by bots, because you don't really need a human to do that. It's very simple. You get the structured data, which is, oh, how did Apple shares do this day? And then you just turn that into sentences, and then you report that on the website. So it's faster, more systematic, and it works. You can also generate text from media data. A much newer thing, but getting some traction now. So for instance you could have a video or an image and you can have your AI take this as an input and then generate a caption describing what's happening and that's great for things that's accessibility, right? So if you're visually impaired, then you can have a little AI describing what's happening in the picture. And then this way you can access a lot of media that would have been inaccessible before.", "Right. Okay, so I have a few slides about basically the evolution of NLP. This is not very detailed. about basically the evolution of NLP. This is not very detailed, but just to give you a rough idea. Early NLP systems focused on rule-based systems. And the way rule-based systems work is that you have an expert writing rules and saying you know if you see this word that means someone is happy if you see that word that means someone is sad. If you see that word, that means someone is sad. If you see this word, you need to report to the police and things like that. And then you have programmers coming, taking those rules and then programming an AI, expert system out of those rules and then they will just send the system back to the expert, they will just test it and say this is terrible, is good whatever change this at this and so on and so forth rulebed systems although I'm making front of them right now are actually very useful and they use quite a lot. You can use things to like extracting elements from text, like dates, names with things you must have seen called regular expressions.", "And then you can do in classify text using stuff we call lexicants, which are just list of terms. And then you can use this and then you're immense programming now-how to kind of build reports or do whatever you want with it. We still use all the systems these days because they are very easy to build. We don't need any data to start with and they're very fast usually. Then we ended up having a lot more data and computational power that we knew what to do with and this is the era of the classical machine learning algorithms. You might have heard things like super vector machines. This is in trees, logistic regression, linear regression and things that that. Those classical machine learning algorithms are still used today. They're very good. They have a good trade-off of like, oh, it takes half an hour to build and it gives you good performance on what you want to do and things like that.", "And it brought in it an obsession with benchmarking. So, has any of you heard of Kaggle? And raise Kaggle? And raise Kaggle? Let me? Really? I'm surprised. I thought you must more prefer than this. Kaggle is a website basically with machine learning competitions where you just basically submit your algorithm and then it benchmarks it against a lot of other algorithms and the winner gets I don't know ten thousand dollars or something so it builds kind of obsession with benchmarking comparing and then a new obsession with building a very strict and formal evaluation methodology for all systems based on data. And that will make a lot more sense in a few lectures where I'm going to talk about this. And my sharing everybody here has at least heard of deep learning. Who wasn't? No, OK, good. Then there was the deal increase, we have so much data, we have so much computation, you know, and that's it and this is the current state of NLP research. Right. A few common subfield of NLP you might encounter if you open a textbook and I'm going to talk about basically what they focus on and it's just to give you an idea of the range of users that NLP algorithm have.", "The first one, one of the simplest one, is opening or send my analysis, depending on who you're reading. And for example, that will be reading a movie review and detecting whether someone liked or disliked the movie. Now this is very useful for instance if you're doing product market research and then you're trying to find out, well, should we fund the next avatar? Everybody loved it, fine, makes a lot of money, whatever. Another one, arguments, tense section. So for given sentences A and B, you want to detect whether A is an agreement with B or disagreement with B, also a very common field. Textual entailment is a bit more difficult. Summarization, a very common one as well. So you encounter summarization on a regular basis if you type a question in Google. And then it spits out an answer above all web pages. Google did not figure out that answer. It extracted this from a page which is, you know, in the documents that you're seeing and then it's just showing it to you directly because it thinks that's what you want to see.", "So this is one of the most common. because it thinks that's what you want to see. So this is one of the most common uses of summarization. Question answering, kind of related, if you ever used Siri or Alexa or or Kratina orartana or whatever. This is what question answering is basically. It has a huge database of facts and things that he can answer and then when he detects a question he just finds out what you want to know and then spits out the answer. That's why if you repeat the same question, it's going to repeat the same answer because you will always map for the same one. In formation retrieval, how much to me everybody here has used Google before, or some equivalent. I don't know if there's any big people here. Usually know, but it can be, it is possible. Comersational user interfaces, so those are the very annoying chatpots I was mentioning before that pop up on all the websites and asking you what they can do to make you buy their stuff. Okay. Now another quick question just as a reflection point.", "How, what common NLP systems do you think you interact with? So I cited Google, so that's kind of an obvious one, but I'm a bit curious to see if any of you have used anything else. Hen raised, answers. Don't let me point. Yes. Sorry? Oh yes. Sorry. you're generating the text that is most likely considering the audio that was received. Yeah? Yeah, exactly. That's another one. Anything else? Sorry? Google Maps. That's also another one. That's a very interesting one because it's not mapping text to anything. It's mapping text to anything is mapping text to geographical entities and it is trying to understand what you're referring to when you say I want to find I don't know aspire cafe right considering what's the closest thing, I know, what time of the day it is, is it 12, maybe you want a cafe, then it's pointing to this or something else.", "Yes? So I can repeat that? Photo upscalers. Do they use text? Okay, you would have said that leave for instance. That's absolutely like a usage of NLP. Everybody here is, sorry? I'm not the use of feature when you can Schenectady's photos, so you take a picture and contrast. optical character recognition. That's also part of NOP, sort of. Yeah. Yeah. Apple pay. When you scan, when you scan what? For example, when you scan what? For example, I was thinking in a sense that how you have your kind of details on your forms? Yeah. You would just kind of adjust all those two systems for you just scan your phone over a car driver that I don't think that that counts as NLP. I thought you were gonna say that's NFC not NLP.", "Near field communication. Yeah, near field communication. I thought you were going to refer to because that's something which is true is that in some cases, I know Google Pay does it, Google Wallet does it, where when you receive a bill in your emails it scans it and then kind of remembers it right so it's telling you you have a bill due on Sunday because it can't the PDF which is very boring. Also useful. Yeah. So as anybody heard of Dali, the image generation thing? Yeah, well that's some of the use of NLP, right? Because Dali takes a natural language description of something and then basically tries to map that to a set of images. So anyway, as you can see, there's a lot of NOP thing that we are using on the today basis.", "There's more than that. I don't know how to, I should have made a list, but if you think about it, like you'll find that it's more common than you think. And to a general question, and that's more of a Henry's kind of thing, how happy are you overall, do they understand you? And if they're the one speaking do you understand them? Not completely there, right? I know in my case Google Assistant is a bit hit and miss. But I think we are making a lot of progress compared to previous years and previous decades and we are similarly getting there. Yeah. right. So that was the. So that was the general overview of NFP. If you're a master students and you want to do more work in NFP, you can come see me and I'll point to the right direction but this is just a general history lesson.", "Now we're going to talk about something called the NOP pipeline and that's something that's going to bother you for at least until coursework one. So pay attention. Some primary notions to understand this, when we talk about documents, you might think it's like a physical document, but when we say document, what we mean is a unit of interest. So if you're making an NRP system and you want to analyze tweets, then a document is a tweet. If you want to analyze books, then document is a tweet. If you analyze books, then document is a box. If you want to analyze the content of a book, there may be a document should be a chapter, or it should be a paragraph, or it should be whatever, it doesn't really matter. It's a unit of interest. When we have this document and we put them into a collection, we call that a corpus or a data set. And you might find these two terms, kind of equivalent in the literature, depending on whether an NFP person or a linguistics person wrote it.", "And the main idea is that it's about the framing of what we want to analyze. The corpus could be anything and a document could also be anything. This is an overview of the pre-processing pipeline in NRP, which I actually wrote for my PhD thesis and I've been using it since then because I like it so much. So as you can see right we are starting from an input so in this case a small piece of text from Wikipedia about the Porter-Staining algorithm. Then we are going for a set of steps basically which helps us kind of cut things off and then put it into different words and then analyze each word so that we have something which can be fed into an LOP algorithm at the end. So we start with tokenization, then annotation, limitation or stemming, stop word filtering, and then we're done. Some of those steps can be skipped. Annotation can be sometimes skipped.", "Limatization can be sometimes skipped, and so one can also skip, but tokenization is the only one that's actually mandatory because to beization refers to actually cutting the text into talk onism and if you don't do that then you haven't really done anything. So let's go through each of these steps one by one. A document is made of tokens, hence the name tokenization, and those tokens can be of arbitrary length, and that depends on what we're trying to analyze. So for instance, if we are trying to, if we care about phrases, so like consecutive bits of text, then tokens could be the doggoran and the catche is there. So there's two subphrases in that sentence. If we care about words, then obviously we're going to put that into words, the dog run and the cat chase them. If we care about syllables, let's say for instance we want to analyze syllables to make a poetry generator which exists.", 'The DORE and the cat check is the in. If you care about characters because we want to make a spelling correction algorithm, right? characters, the HEGE space, and so on, I think you can them into characters, THE space, DoG space, and so on. I think you get the point. We usually care about words, but sometimes we care about pairs of words, sometimes we care about phrases. It really depends on what we are trying to do. The next step is annotation and by annotation what we mean is that we want to enrich all those tokens with what we know about them. Usually we do it with part of speech, part of speech being the grammatical function of the word in the sentence. So as you may guess, part of speech depends on the language that is used, right? Part of speech in English, French, or Chinese are very different.', "Also, even within languages, you will see that there are different kind of of parts of speech classifications. So it's a very complicated thing. Thankfully, you don't have to understand the actual part of speech. You can just use it. Right. What we use about to speech for is that sometimes we won't help to disambigorate meaning using the grammatical context. So for example if I gave this sentence the sailor dogs the hatch, then if you just took dogs separate from anything else, then you would think immediately like this is referring to the animal and you just classify that with the rest of the animals words. Except that is not the case here because here dogs is the verb which means to close the door and secure them in a close position. So you see here context, knowing that it's a verb, help you actually understand the meaning of that word in that context, which helps you down the line in the NFP guideline.", "Next step, we call usually awards analyzation and usually refers to one or two things which is either limitizing or stemming. So as we know, words are inflected during language during usage, sorry. So for example, here, when you have a verb like B right you don't say I be happy I be hungry You inflect that which means is modified based on the rest of the sentence. You say, I am happy, or I am hungry, or he is happy, or whatever. And the goal of standardization is to remove this inflection. We want to know what is the core word, the core now, the core verb that is referred to by the inflected now. So if you have something which is plural, you want it to be mapped to the same word if it's singular. If you have dogs and dog in the same sentence and they're both nouns, you want them to be together. So the way we do this is either lematization or stemming. When we limitize things we are reducing terms to their lemma which is the dictionary form and the way it which is the dictionary form.", "And the way it works is that you have a very complicated algorithm that goes through each word and then based on the part of speech and the word itself. It says, this is referring to the verb dog or this is referring to the non dog or this is referring to whatever. So that's a very complex algorithm and the other one is stemming, which is reducing terms of the word stem and that's just basically a very simple algorithm that just cuts off anything that looks like it's an inflection. So it will give you results which are going to be, we're going to sound terrible, like not like words, but for the sake of the algorithm, it's more than enough. So an example here, leimatization will map dogs as dog, dog as dog, and then dog is dog, right? So upper case, lower case, doesn't matter. It's all mapped the same word. So it produces very consistent conduct, but because it has this big dictionary thing it's always looking at, it's always looking at is very slow and also it requires to be part of speech annotated because it needs the context of the sentence the grammatical context to do its job. On the other hand, stemming would map programming to program, programmer to to program with two M's, which is obviously not great, but there's a bit of noise but overall it works close enough that it's actually good enough for the application so that it's a lot of words that don't exist, but it's a lot faster and sometimes that's what you need.", 'And the way it works is just basically run a bunch of transformation on each token in order to get that result. Filtering, I think is the last step, yes. Not all words matter equally, as you might have guessed. Some words like determinants for instance are not really useful for any NFP purpose like the the dog for instance who cares about the. This actually gives you any information. And what we want to do when we build NFP models is that we want to have the smallest model possible that can do the job. And that means removing this kind of noise. So the way we do this is that we have this list of words in every language called the stop list, and the words called the stop words. Not sure why actually. And any word which is in this list usually gets removed from the text during this last step.', "We can also filter words by frequency, so words which are too frequent, which means they are in all documents, are not very useful, and the words which only appear once usually are not useful either. So we cut them off. We'll see more about this in the coming weeks. This is just like an introduction to get your coin data with the vocabulary that we're going to use. And finally, and I mentioned this a bit before, sometimes we care about sets of words and not words themselves. So for example, Big Ben or Empire State Building would lose all meaning if we isolated every single word separately, right? Big and Ben, a little of a dumb thing, embarrassed the ability and the same thing. But if we look at the pair or the triple of words, then we know what is referring to. He is referring to the pigtours, referring to the big building, right? And in that case, what we do is that we actually extend our thing.", "And instead of just looking at isolated words, we look at pairs of consecutive words. We call that n-grams, and unigram being single words, bi-grams being pairs of consecutive words, trigrams, tri-grams, tri-igrams, triples, and you get the idea. Right, and I think I blizzed through this lecture much better than I thought. And here I was moving on that. Some reading to do, because I know is one thing, is that students love homework. This is very cool paper. What are very cool paper? What am I saying? This is paper called Eliza. And this is a very important paper because this is one of the first kind of, you know, mainstream NOP systems. And it was in 1966. I mean, you weren't born, I was unborn, Joe was unborn either, right? And the stuff they were doing with computers that are less powerful than your Apple watch is incredible.", "And you don't need to read into details, right? But if you look at a PDF and have a quick look at the way they are using transformation rules to take the input text and then turn that into a very convincing output text to imitate an actual person is very interesting. You don't have to read the details, it's more of a point of interest. And I think that's it for now. I'm going to, yeah, shoot another recording the questions or is there any questions? No question. Please just a few more minutes. You're almost close to the end, don't worry. Any question about the... Oh, sorry. Yes. So I'm just as the internet. The one process for NOP if I'm able to able to distinguish between whatever, obviously it spells something wrong, it's going to say like, if it's a real line, it's not that wrong.", "It is not an LP system, but it does have NOP system so the spelling character in your Microsoft Word is yet another kind of small AI embedded into your computer that's telling you you know this is wrong this is wrong yeah I'm sorry I can't hear that. I'm sorry I can't hear. And I'd be like the main problem that any items in the book I wouldn't see the base. Yeah. Yeah. Quiet, please. Yeah, it's almost the end, just, you know, calm down. I will do though, you say the basis, the word spelling correction in Microsoft Word, for instance, is very complex. The one we used to have, like 10 years ago, was just random dictionary search, but the one now is actually quite a beast comparatively yeah so you went there first I'm sorry I'm sorry I'm sorry I'm sorry this one filter oh it's a box what is my working now okay this one.", "This one? Before that? Oh, this is not part of the process. This is not part of the process. It's just like an additional note that sometimes we don't actually analyze isolated words, we are taking them into pairs and things like that. Yeah. Sorry. You're going to see more about this in the labs because we're gonna deal directly with this. Yeah, sorry? Would you ever do like a position before adaptations to find the meeting of the base of the base members? adaptation before the annotation? No, because when you limitization before the annotation? No, because when you lematize, right, you are actually losing the grammatical effect, because since you remove the inflection, right, then you remove stuff. the conflict because since you remove the inflection, right? Then you remove stuff which helps you know what's the role of that word in the sentence. And you need the part of speech to the delimatization.", "So you can't have it before. Does that make sense? Right, because it is through the part of speech that the lematizer knows that, oh, this is the verb, so it needs to be limatized that way, or this is the noun, limatized that way. That makes sense, yeah. OK. That makes sense. Yeah. Okay. Any other pending questions except. Sorry. Yeah. accept. you mean stemming? Okay, so the limitation. Okay, so theization uses a dictionary. So it's always going to give you the dictionary form of a word. It might be wrong, it might be correct, but the word you get has an output is always an actual word which exists.", "And for that reason, it takes a bit of time because basically there's a lot of process to analyze and find out what is the most likely dictionary form of that word. On the other hand, the way stemming works, right, is that you have a set of rules which says, oh, if this things ends with an S, cut the S, if you end with E S, cut the E S, and then switch to the next step, and then if there is two M's, remove one M, so there's a bunch of rules which acts at a character level so it just looks at a set of characters and applies a set of rules to transform it and get you something which hopefully is the close to the dictionary form. to something of that word. the next question of the process of the process uses the engineering form, well, will be used to the dictionary form. a process users that need to learn well-to-value is something that you can be quiet. Saving time. Sometimes you don't care if you make like, if 5% of your thing making mistake because you can process twice as much data in the same amount of time.", "In the end, a lot of the shortcuts we take in machine learning are about saving time. When we cut off words because they're not frequent enough, we're also trying to save time. You're just trying to make the process as easy as possible for the algorithm at the end because getting doing more in a same amount of time is extremely valuable You know sometimes he takes what maybe not these days, but like sometimes it takes days and weeks to train a model and if you can cut that by five days just very nice Yeah and just very nice. And also sometimes it doesn't matter. If you have a word if it doesn't exist, maybe it's no important. Okay. Any chance. Yeah. Yeah. Yeah. I'm sorry, I didn't hear. Data.", "Oh, we'll be taking data from all around the web. Don't worry, that's going to be part of the lab. Right? So I am still finishing up some details on the lab, so I haven't really yet but don't worry is tomorrow from 4 to 6 best time. Yeah? The lab. Yeah. Yeah. Everything is always on the moodle before the actual time. with the session rather, so everything's always going to be during the time, not for. Right. All right, get out. Oh,"] 

values = []
# iterate over transcript and compute similarity once
for i, chunk in enumerate(chunks):
    sim = compute_cosine_similarity(chunk, slide_text)
    values.append((i, sim))

# Calculate median based on sorted values
median = statistics.median([sim for i, sim in values])

removed_chunks_indexes = [i for i, sim in values if sim < median]

print("Removed chunks indexes:", removed_chunks_indexes)


