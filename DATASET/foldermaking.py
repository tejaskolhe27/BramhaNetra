import os

barakhadi = ['क ', 'का ', 'कि ', 'की ', 'कु ', 'कू ', 'के ', 'कै ', 'को ', 'कं ',
    'ख ', 'खा ', 'खि ', 'खी ', 'खु ', 'खू ', 'खे ', 'खै ', 'खो ', 'खं ',
    'ग ', 'गा ', 'गि ', 'गी ', 'गु ', 'गू ', 'गे ', 'गै ', 'गो ',  'गं ',
    'घ ', 'घा ', 'घि ', 'घी ', 'घु ', 'घू ', 'घे ', 'घै ', 'घो ',  'घं ',
    'च ', 'चा ', 'चि ', 'ची ', 'चु ', 'चू ', 'चे ', 'चै ', 'चो ',  'चं ',
    'छ ', 'छा ', 'छि ', 'छी ', 'छु ', 'छू ', 'छे ', 'छै ', 'छो ',  'छं ', 
    'ज ', 'जा ', 'जि ', 'जी ', 'जु ', 'जू ', 'जे ', 'जै ', 'जो ',  'जं ',
    'झ ', 'झा ', 'झि ', 'झी ', 'झु ', 'झू ', 'झे ', 'झै ', 'झो ',  'झं ', 
    'ट ', 'टा ', 'टि ', 'टी ', 'टु ', 'टू ', 'टे ', 'टै ', 'टो ', 'टं ', 
    'ठ ', 'ठा ', 'ठि ', 'ठी ', 'ठु ', 'ठू ', 'ठे ', 'ठै ', 'ठो ', 'ठं ', 
    'ड ', 'डा ', 'डि ', 'डी ', 'डु ', 'डू ', 'डे ', 'डै ', 'डो ','डं ', 
    'ढ ', 'ढा ', 'ढि ', 'ढी ', 'ढु ', 'ढू ', 'ढे ', 'ढै ', 'ढो ','ढं ', 
    'ण ', 'णा ', 'णि ', 'णी ', 'णु ', 'णू ', 'णे ', 'णै ', 'णो ','णं ',
    'त ', 'ता ', 'ति ', 'ती ', 'तु ', 'तू ', 'ते ', 'तै ', 'तो ','तं ',
    'थ ', 'था ', 'थि ', 'थी ', 'थु ', 'थू ', 'थे ', 'थै ', 'थो ','थं ', 
    'द ', 'दा ', 'दि ', 'दी ', 'दु ', 'दू ', 'दे ', 'दै ', 'दो ', 'दं ',
    'ध ', 'धा ', 'धि ', 'धी ', 'धु ', 'धू ', 'धे ', 'धै ', 'धो ','धं ',
    'न ', 'ना ', 'नि ', 'नी ', 'नु ', 'नू ', 'ने ', 'नै ', 'नो ', 'नं ',
    'प ', 'पा ', 'पि ', 'पी ', 'पु ', 'पू ', 'पे ', 'पै ', 'पो ', 'पं ',
    'फ ', 'फा ', 'फि ', 'फी ', 'फु ', 'फू ', 'फे ', 'फै ', 'फो ', 'फं ',
    'ब ', 'बा ', 'बि ', 'बी ', 'बु ', 'बू ', 'बे ', 'बै ', 'बो ', 'बं ', 
    'भ ', 'भा ', 'भि ', 'भी ', 'भु ', 'भू ', 'भे ', 'भै ', 'भो ','भं ', 
    'म ', 'मा ', 'मि ', 'मी ', 'मु ', 'मू ', 'मे ', 'मै ', 'मो ','मं ',
    'य ', 'या ', 'यि ', 'यी ', 'यु ', 'यू ', 'ये ', 'यै ', 'यो ', 'यं ', 
    'र ', 'रा ', 'रि ', 'री ', 'रु ', 'रू ', 'रे ', 'रै ', 'रो ','रं ', 
    'ल ', 'ला ', 'लि ', 'ली ', 'लु ', 'लू ', 'ले ', 'लै ', 'लो ','लं ',
    'व ', 'वा ', 'वि ', 'वी ', 'वु ', 'वू ', 'वे ', 'वै ', 'वो ','वं ', 
    'श ', 'शा ', 'शि ', 'शी ', 'शु ', 'शू ', 'शे ', 'शै ', 'शो ','शं ',
    'स ', 'सा ', 'सि ', 'सी ', 'सु ', 'सू ', 'से ', 'सै ', 'सो ','सं ',
    'ह ', 'हा ', 'हि ', 'ही ', 'हु ', 'हू ', 'हे ', 'है ', 'हो ', 'हं ',
    'ष','षा',' षि',' षी',' षु ','षू ','षे ','षै ','षो ','षं',
    'अ ', 'आ ', 'इ ', 'उ ', 'ए ', 'ओ ']


# Specify the parent directory where you want to create the folders
parent_directory = "page3"

# Create folders
for folder_name in barakhadi:
    folder_path = os.path.join(parent_directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Folder '{folder_name}' created at '{folder_path}'")



