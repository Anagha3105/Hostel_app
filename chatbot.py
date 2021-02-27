
def answering(question):
	#defining keywords
	fee = ['fee', 'cost', 'price', 'pay']
	application = ['appl', 'join', 'form']
	amenities = ['amen', 'facilit', ]
	rules = ['rule']
	leave = ['leave', 'vacation', 'absent', 'holiday']
	guardian = ['parent', 'guardian', 'lg']
	guest = ['visitor', 'guest']
	location = ['location','address','distance']
	transport = ['transport','bus','route']
	curfew = ['tim', 'curfew'] #is tim fine? or wld it raise issues later?
	food = ['food','menu']
	laundry = ['laundry', 'wash']
	internet = ['wifi','net']
	covid = ['covid','corona','pandemic','hygiene','mask','social', 'distancing','quarantine']
	rules = ['rule'] #http://www.livingspaceblr.com/rules-and-regulations/
	 

	#Getting input and converting it all to lowercase, to compare easily
	#t = (input("Hey! Welcome to PESU RR Girls Hostel Portal. How may I help you today! \n")).lower()
	t=question.lower()
	
	#Finding keywords to link to appropriate answer
	for i in fee:
		if i in t:
		    answer="Check out http://www.livingspaceblr.com/wp-content/uploads/2020/03/Fee-for-fresh-batch-2020-21-RR-Campus.pdf"
		    

	for i in application:
		if i in t:
		    answer="Check out http://web.archive.org/web/20191030074249/http://www.livingspaceblr.com/download-application-form/"

	for i in amenities:
		if i in t:
		    answer="""•A private and secured stay, with very high level security. 
        •Facilities for reading and entertainment.
        •Optional accommodation facility on single or shared bases.
        •Best of facilities with respect to maintenance and services.
        •Hygenic Food.
        •Transportation facility – from hostel to college and back to hostel.
        •Bio-metric Attendence system to make the presence of students tranparent.
        •CCTV camera survillence for the security of students at the premises of the hostel.
        •Beds with mattresses.
        •Built-in wardrobes.
        •Study chairs.
        •The hostel authorities shall arrange for clear, hygienic drinking water, 24 hours a day.
        """

	for i in rules:
		if i in t:
		    answer="Check out http://www.livingspaceblr.com/rules-and-regulations/"

	for i in leave:
		if i in t:
		    answer="If any student is staying away from the hostel for any valid reason, they should seek prior permission from the hostel in-charge/warden. Use this form"

	for i in guardian:
		if i in t:
		    answer="Local guardian (LG) should be above 35 years of age. Parents have to authorise the LG. If in case the LG is student's own brother/sister, rules may be relaxed. LG will have to respond to the request of hostel authorities from time to time. LG must know english. Identified LG should be introduced to the warden. Use this form"

	for i in guest:
		if i in t:
		    answer="No guests are allowed to enter the hostel without prior permission of warden, including relatives. They can only meet their ward in the reception. Visitors other than parents may not be allowed unless the warden is convinced. Warden's decision is final and binding."

	for i in location:
		if i in t:
		    answer="All hostels are managed by PES. The boys’ hostel is within the campus. The girls’ hostel is about 2 Km distance from campus for which college buses are available."


	for i in transport:
		if i in t:
		    answer="Check out http://www.livingspaceblr.com/bus-route-to-living-space/"

	for i in curfew:
		if i in t:
		    answer="7pm to 7am are study hours. Every student should strictly be in their rooms, except when they go for dinner. Students are not allowed to go to other rooms. Students are not allowed to go out without the permission of the warden during this time."
	for i in food:
		if i in t:
		    answer="Food is provided according to a regular menu fixed by the college management. The menu is a mix of north and south Indian cuisines. Requests from the students to change the menu will not be entertained."

	for i in laundry:
		if i in t:
		    answer="A permanent laundry service is available at both boys’ and girls’ hostels."

	for i in internet:
		if i in t:
		    answer="Both boys' and girls' hostels are wifi enabled."

	for i in covid:
		if i in t:
		    answer="All students must submit negative COVID 19 RTPCR test taken within 72 hours before they move into the hostel. All social distancing measures are being followed. Common spaces are routinely sanitised. Students must wear a mask in common spaces. Canteen is provided with plastic barriers to prevent spread of disease. Temperature is checked for everyone before entering the hostel. PES or Living Spaces is not responsible if student catches COVID 19 from the hostel."
	return answer


from tkinter import *                                             
                                                                    
root = Tk()                             
user = StringVar()                          
bot  = StringVar()                          
                                    
root.title(" Hostel Info ChatBot ") 

l1 =Label(root, text=" User : ")
l1.grid(row = 0, column = 0)                
user_entry=Entry(root, width = 100, borderwidth = 5, textvariable=user)
user_entry.grid(row = 0, column = 1)   
	                             
def main():                             
       question = user.get() 
       ans = answering(question)
       
       bot.set(ans)                       
      
b1 = Button(root, text="Answer", command=main)
b1.grid(row = 0, column = 2)        
Label(root, text=" Bot  : ").grid(row = 1, column = 0)                             
t=Entry(root, width = 100, borderwidth = 5, textvariable = bot)
t.grid(row = 1, column = 1)
       
                                   
root.mainloop() 
