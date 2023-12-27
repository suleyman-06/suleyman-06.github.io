attendance = int(input("please enter the students attendance in %"))
if attendance >90:
  Score = int(input("Enter the students total marks"))
  
  if  Score>90:
     print("this student has achieved an A")
  elif Score>80 and Score <= 90:
     print("this student has achieved a B")
  elif Score>70 and Score <=80:
     print("this student has achiveed a grade C")
  else:
     print("FAIL!")
else:
  print("This student has failed due to their poor attendance")
