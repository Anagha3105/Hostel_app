
#Referencing lists
#using half the word so that it includes all possible ways of that word. like 'shar' will include 'share', 'sharing' etc.
female = ['girl', 'female', 'wom', 'lady']
male = ['boy', 'male', 'man', 'men']
fee = ['fee', 'cost', 'price', 'pay']
application = ['appl', 'join', 'form']
amenities = ['amen', 'facilit', ]
sharing = ['mate', 'shar', ]
block = ['1', 'first', '2', 'second', '3', 'third', '4', 'fourth', 'where', 'block', 'building']
rules = ['rule'] #http://www.livingspaceblr.com/rules-and-regulations/

#Getting input and converting it all to lowercase, to compare easily
a = (input("Hey! Welcome to PESU RR Girls Hostel Portal. How may I help you today! \n")).lower()
inp = a.split()

#defining fucntions

if inp in fee:
    print("Check out http://www.livingspaceblr.com/wp-content/uploads/2020/03/Fee-for-fresh-batch-2020-21-RR-Campus.pdf")
if inp in application:
    print("Check out http://web.archive.org/web/20191030074249/http://www.livingspaceblr.com/download-application-form/")
if inp in amenities:
    print("""•	A private and secured stay, with very high level security. 
    •	Facilities for reading and entertainment.
    •	Optional accommodation facility on single or shared bases.
    •	Best of facilities with respect to maintenance and services.
    •	Hygenic Food.
    •	Transportation facility – from hostel to college and back to hostel.
    •	Bio-metric Attendence system to make the presence of students tranparent.
    •	CCTV camera survillence for the security of students at the premises of the hostel.
    •	Beds with mattresses.
    •	Built-in wardrobes.
    •	Study chairs.
    •	The hostel authorities shall arrange for clear, hygienic drinking water, 24 hours a day.
    """)
if inp in rules:
    print("Check out http://www.livingspaceblr.com/rules-and-regulations/")

'''
while True:
    try:
        gender = (input("Enter gender of your ward: \n")).lower()
        if gender in female:
            fem()
            break;
        elif gender in male:
            mal()
            break;
        else:
            print("Invalid input, try again.")
    except:
        continue
'''
'''
while True:
  try:
    gender = input("Enter gender: ")
    if gender == "Male" or gender == "Female":
      print("Gender entered successfully...")
      break;
    else:
      print("Gender should be either Male or Female")   
  except:
    continue
'''

