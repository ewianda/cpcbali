from users.models import Boban
from dictionary.models import Word
g = lipsum.Generator()
users = []
words=[]
 
for i in range(100):
    user = Boban(first_name='User%dFirstName' % i, 
                last_name='User%dLastName' % i,
                email='user%d@mydomain.com' % i,
                password='hashedPasswordStringPastedHereFromStep1!',
                is_active=True, 
                )
    users.append(user)
    w=g.generate_paragraph()
    word=  Word(user = user,word=g.dictionary[-i], definition=g.generate_paragraph())
    words.append(word)
Word.objects.bulk_create(words)
#Boban.objects.bulk_create(users)

for i in range(100):
    if i==0:
      continue
    user = Boban.objects.get(pk=i)
    if not user.id:
      continue
    users.append(user)
    w=g.generate_paragraph()
    word=  Word(user = user,word=g.dictionary[-i], definition=g.generate_paragraph())
    word.save()
    #print word.user.id
    #words.append(word)
Word.objects.bulk_create(words)
#Boban.objects.bulk_create(users)
