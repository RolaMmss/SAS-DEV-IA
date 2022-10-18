# Fort de votre expérience en pâtisserie, vous décidez de créer un forum en ligne pour parler de gâteaux ! 
# - Vous devez définir et instancier trois classes: Utilisateurs (et ses héritiers), fil de discussion et post (et ses héritiers)


# Sur ce forum
# - les utilisateurs fans de pâtisserie pourront : s’inscrire et se connecter ;
# - parler de leurs gâteaux préférés, en créant de nouveaux fils de discussion ;
# - répondre à des messages, dans les fils existants.
# 
# - Un fil de discussion sur ce forum a un titre, une date de création et une collection de posts lui correspondant.
# - Chaque post contient du texte, l’utilisateur qui l’a publié et la date de publication.
# - Les utilisateurs ont la possibilité d’attacher des fichiers à leurs posts :
# - Partez du principe qu’il peut y avoir de nombreux types de fichiers, mais nous sommes surtout intéressés par les fichiers images (GIF ou JPEP).

# - Un post peut avoir un fichier attaché, ce qui changera la façon dont le post est affiché. Ce serait donc un nouveau type de post.

# - Enfin, il y a des utilisateurs spéciaux nommés modérateurs, qui ont la capacité de modifier un post pour qu’il contienne du contenu nouveau, et de supprimer ceux qui ne parlent pas de gâteaux. ;)


import datetime
datetime.datetime.now()

class User:
    def __init__(self,status = "non inscrit"):
        self.status = status

    def sign_up(self,name,email,mdp):
        self.name = name
        self.email = email
        self.mdp = mdp
        self.status = "inscrit"
        print("l'utilisateur est maintenant inscrit")

    def sign_in(self,email_from_form,mdp_from_form):
        if self.status == "non inscrit":
            return "utilisateur non inscrit"
        else:
            if self.email == email_from_form and self.mdp == mdp_from_form:
                print("l'utilisateur est maintenant connecté")
                self.status = "connecté"
            else:
                print("l'email ou le mot de passe ne correspond pas aux données de l'utilisateur")

    def new_fil(self,titre):
        if self.status == "connecté":
            return Fil(titre)
        else:
            print("seul les utilisateurs connectés peuvent créer des nouveaux fils")

    def new_post(self,fil,content,jpeg_file_path=False,gif_file_path=False):
        if self.status == "connecté":
            if jpeg_file_path:         
                jpegpost = JpegPost(content,self.name,jpeg_file_path)
                fil.post_collection.append(jpegpost)
                print("un post jpeg a été créé")
                return jpegpost

            elif gif_file_path:
                gifpost = GifPost(content,self.name,gif_file_path)
                fil.post_collection.append(gifpost)
                print("un post gif a été créé")
                return gifpost

            else:
                normalpost = Post(content,self.name)   
                fil.post_collection.append(normalpost)
                print("un post normal a été créé")  
                return normalpost     
        
        
        else:
            print("seul les utilisateurs connectés peuvent créer des nouveaux posts")


class Moderator(User):
    def update_post(self,post,new_content):
        post.content = new_content

    def delete_post(self,fil,index_post_a_supprimer):
        fil.post_collection.pop(index_post_a_supprimer)

class Fil:
    def __init__(self,titre, creation_date=datetime.datetime.now(),post_collection=[]):
        self.titre = titre
        self.creation_date = creation_date
        self.post_collection = post_collection
    
    def __str__(self):
        return f"{self.titre}, créé le {self.creation_date}, contient {len(self.post_collection)} messages \n {self.post_collection}"


class Post:
        def __init__(self,content, author,publication_date=datetime.datetime.now()):
            self.content = content
            self.author = author
            self.publication_date = publication_date
        
        def __str__(self):
            return f"{self.content[:10]}, auteur {self.author}"

        def __repr__(self):
            return f"{self.content[:10]}, auteur {self.author}"

class JpegPost(Post):
        def __init__(self,content, author,jpeg_file_path, publication_date=datetime.datetime.now()):
            super().__init__(content, author,publication_date)
            self.jpeg_file_path = jpeg_file_path


class GifPost(Post):
        def __init__(self,content, author,gif_file_path, publication_date=datetime.datetime.now()):
            super().__init__(content, author,publication_date)
            self.jpeg_file_gif = gif_file_path


charles = User()

print(charles.status)

charles.sign_up("charles","charles@gmail.com","secret")
charles.sign_in("charles@gmail.com","secre")
charles.sign_in("charles@gmail.com","secret")

nouveau_fil = charles.new_fil("mes gateaux préférés")

print(nouveau_fil)

nouveau_post = charles.new_post(nouveau_fil,"pour vous quel est le meilleur gateau",gif_file_path="http//file_path/gif")
charles.new_post(nouveau_fil,"surper idéee")


print(nouveau_post.publication_date)

print(nouveau_fil)

superuser = Moderator()

superuser.update_post(nouveau_post,"nouveau contenu")
print(nouveau_post)
print(nouveau_fil)


superuser.delete_post(nouveau_fil,1)
print(nouveau_fil)