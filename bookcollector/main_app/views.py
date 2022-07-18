from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#  ------- CLASS ----------------------------------

# Add the Books class & list and view function below the imports
class Book:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, author, series, description):
    self.name = name
    self.author = author
    self.series = series
    self.description = description

books = [
  Book('Harry Potter and the Sorcerer''s Stone', ' J.K. Rowling', 'Harry Potter', 'Harry Potter''s life is miserable. His parents are dead and he''s stuck with his heartless relatives, who force him to live in a tiny closet under the stairs. But his fortune changes when he receives a letter that tells him the truth about himself: he''s a wizard. A mysterious visitor rescues him from his relatives and takes him to his new home, Hogwarts School of Witchcraft and Wizardry. After a lifetime of bottling up his magical powers, Harry finally feels like a normal kid. But even within the Wizarding community, he is special. He is the boy who lived: the only person to have ever survived a killing curse inflicted by the evil Lord Voldemort, who launched a brutal takeover of the Wizarding world, only to vanish after failing to kill Harry. Though Harry''s first year at Hogwarts is the best of his life, not everything is perfect. There is a dangerous secret object hidden within the castle walls, and Harry believes it''s his responsibility to prevent it from falling into evil hands. But doing so will bring him into contact with forces more terrifying than he ever could have imagined. Full of sympathetic characters, wildly imaginative situations, and countless exciting details, the first installment in the series assembles an unforgettable magical world and sets the stage for many high-stakes adventures to come.'),
  Book('Twilight', 'Stephenie Meyer', 'The Twilight Saga', 'About three things I was absolutely positive. First, Edward was a vampire. Second, there was a part of him—and I didn''t know how dominant that part might be—that thirsted for my blood. And third, I was unconditionally and irrevocably in love with him. Deeply seductive and extraordinarily suspenseful, Twilight is a love story with bite.'),
  Book('Fifty Shades of Grey', 'E.L. James', 'Fifty Shades', 'When literature student Anastasia Steele goes to interview young entrepreneur Christian Grey, she encounters a man who is beautiful, brilliant, and intimidating. The unworldly, innocent Ana is startled to realize she wants this man and, despite his enigmatic reserve, finds she is desperate to get close to him. Unable to resist Ana''s quiet beauty, wit, and independent spirit, Grey admits he wants her, too—but on his own terms. Shocked yet thrilled by Grey''s singular erotic tastes, Ana hesitates. For all the trappings of success—his multinational businesses, his vast wealth, his loving family—Grey is a man tormented by demons and consumed by the need to control. When the couple embarks on a daring, passionately physical affair, Ana discovers Christian Grey''s secrets and explores her own dark desires. Erotic, amusing, and deeply moving, the Fifty Shades Trilogy is a tale that will obsess you, possess you, and stay with you forever. This book is intended for mature audiences.')
]







#  --- DEFINE VIEWS -----------------------------
 
 
#  Home View
def home(request):
    return HttpResponse('Home Page')

# About View
def about(request):
    return render(request, 'about.html')


# Books Index View
def books_index(request):
    return render(request, 'books/index.html', { 'books': books})