# Kaun Banega Crorepati (KBC)
# You can add your own Q & A 
questions = ["Which animal is known as the 'Ship of the Desert'?: ","How many days are there in a week?: ","How many letters are there in the English alphabet?: ","Rainbow consist of how many colours?: ","How many days are there in a year?: ","How many minutes are there in an hour?: "," How many seconds are there in a minute?: ","How many consonants are there in the English alphabet?: ","Name the National bird of India?: ","Name the biggest continent in the world?: ","How many continents are there in the world?: ","Name first of the primary colour?: ","Which colour symbolises peace?: ","Sun rises in the.....: "]

answers = ["camel","7","26","7","365","60","60","21","peacock","asia","7","red","white","east"]

price = ["1000","3000","5000","10000","25000","50000","100000","250000","500000","1000000","2500000","5000000","10000000","70000000"]

i=0
while i<len(questions):
  ans=input(questions[i])
  if ans.lower() == answers[i]:
    print("\ncorrect "+ price[i]+" won \n")
  else:
    print("\n😞 sorry thats wrong answer.\naur Ye gaye "+ price[i] +" rupaye seedha apke bank account me!\n")
    break
  i=i+1  
