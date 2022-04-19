def replace_domain(email,old_domain,new_domain):#define replacedomain function, accepts three parameters to be checked, the email address
                                                # to be checked, the old domain of the email address and the new domain of the email address
    if '@' + old_domain in email: #first check is to see if old domain comes after the @ sign, if true:
      index = email.index('@' + old_domain) # finds where the index of the old domain including the @ starts at (abcd[@olddomain.org])
      new_email = email[:index] + '@' + new_domain #this contains the first half of the portion of the email before the @, then replaces
                                                   #the '@' and old_domain with a new '@' plus new_domain
      return 'updated to '+ new_email #returns new email                            
    return email #if email didnt contain old_domain, return email
  
  
old_domain = 'olddomain.org'
new_domain = 'newdomain.org'

