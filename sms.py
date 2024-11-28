db={1:{'name':'saurabh','city':'indapur','percentage':87,'cource':'python','passing_year':2024}}
print('-'*100)
print(f"{' '*30}Art Commerce And Science Collage")
print('-'*100)
while True:
    print("""
            \t\t\t\t   Dashboard
        
        \t\t\t\t1.add student details
        \t\t\t\t2.display details
        \t\t\t\t3.update stu details
        \t\t\t\t4.delete stu detail
        \t\t\t\t5.filter

    """)
    ch=int(input('enter your choice:'))
    if ch==1:
        rollno=int(input('enter roll no:'))
        name=input('Enter name:')
        city=input('enter city:')
        per=eval(input('enter percentage:'))
        course=input('enter course:')
        passing_year=int(input('enter year:'))
        db[rollno]={'name':name,'city':city,'percentage':per,'cource':course,'passing_year':passing_year}
        print('add successfully...')
    elif ch==2:
        print('-'*97)
        print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('rollno','name','city','percentage','course','passing_year'))
        print('-'*97)
        for rno in db:
          print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(rno,db[rno]['name'],db[rno]['city'],db[rno]['percentage'],db[rno]['cource'],db[rno]['passing_year']))
          print('-'*97)
        
    elif ch==3:
        print('how you can update')
        print(""" 
                  1.name          
                  2.city
                  3.percentage    
                  4.course
                  5.passing_year
              """)
        ch=int(input('enter choise:'))
        rn=int(input('enter rn:'))
        if rn==rno:
          
         if ch==1:
            
            na=input('enter name:')
            db[rno]['name']=na
            print('update successfully...')
         elif ch==2:
            ci=input('enter city:')
            db[rno]['city']=ci
            print('update successfully...')
         elif ch==3:
            perce=eval(input('enter percentage:'))
            db[rno]['percentage']=perce
            print('update successfully...')
         elif ch==4:
            cour=input('enter cource:')
            db[rno]['cource']=cour
            print('update successfully...') 
         elif ch==5:
            py=int(input('passing year:"'))
            db[rno]['passing_year']=py
            print('update successfully...') 
         else:
            print('invalid ')
    elif ch==4:
        ro=int(input('roll number:'))
        del db[rno]
        print('delete successfuly....')
    elif ch==5:
        print("""
               1.name    
               2.city
               3.percentage
               4.course
               5.passing year
             """)
        ch=int(input('choose filter: '))
        if ch==1:
           na=input('enter name:')
           if na==db[rno]['name']:
               print('-'*97)
               print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('rollno','name','city','percentage','course','passing_year'))
               print('-'*97)
               for rno in db:
                print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(rno,db[rno]['name'],db[rno]['city'],db[rno]['percentage'],db[rno]['cource'],db[rno]['passing_year']))
                print('-'*97)
              
            
        elif ch==2:
            city=input('enter city:')
            if city==db[rno]['city']:
               print('-'*97)
               print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('rollno','name','city','percentage','course','passing_year'))
               print('-'*97)
               for rno in db:
                print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(rno,db[rno]['name'],db[rno]['city'],db[rno]['percentage'],db[rno]['cource'],db[rno]['passing_year']))
                print('-'*97)
              
              
            
        elif ch==3:
         percentage=eval(input('enter percentage:'))
         if percentage==db[rno]['percentage']:
               print('-'*97)
               print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('rollno','name','city','percentage','course','passing_year'))
               print('-'*97)
               for rno in db:
                print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(rno,db[rno]['name'],db[rno]['city'],db[rno]['percentage'],db[rno]['cource'],db[rno]['passing_year']))
                print('-'*97)
               
              
        elif ch==4:
         cou=input('enter cource:')
         if cou==db[rno]['cource']:
               print('-'*97)
               print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('rollno','name','city','percentage','course','passing_year'))
               print('-'*97)
               for rno in db:
                print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(rno,db[rno]['name'],db[rno]['city'],db[rno]['percentage'],db[rno]['cource'],db[rno]['passing_year']))
                print('-'*97)
               
              
        elif ch==5:
         pe=int(input('enter passing year:'))
         if pe==db[rno]['passing_year']:
               print('-'*97)
               print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('rollno','name','city','percentage','course','passing_year'))
               print('-'*97)
               for rno in db:
                print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(rno,db[rno]['name'],db[rno]['city'],db[rno]['percentage'],db[rno]['cource'],db[rno]['passing_year']))
                print('-'*97)
               
             
        else:
         print('invalid filter')

        print('filter successfully:') 
         

   
    ch=input('you can back dashboard option:(yes\no)')
    if ch=='no':
      break