class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.owner = owner
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
  
  def __repr__(self):
    return '%s. "%s". %s, %s. %s, %s.' % (self.artist, self.title, self.medium, self.year, self.owner.name, self.owner.location )


class Marketplace:
  def __init__(self):
    self.listings = []

  def add_listing(self, new_listing):
    self.listings.append(new_listing)
  
  def remove_listing(self, expired_listing):
    self.lisitngs.remove(expired_listing)

  def show_listings(self):
    for listing in self.listings:
      print(listing)


class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    if is_museum:
      self.location = location
    else:
      self.location = "Private Collection"
    
  def sell_artwork(self, artwork, price):
    self.artwork = artwork
    self.price = price
    if(self.artwork.owner == self):
      new_listing = Listing(artwork, price, self)
      veneer.add_listing(new_listing)
  
 





      
      

class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller

  def __repr__(self):
    return 'The name of the work of the art %s. The price of the work of art %s' %(self.art.title, self.price)


edytta = Client("Edytta Halpirt", None, False)
moma = Client("The MOMA", "New York", True) 



girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Teellier)", 1910, "oil on canvas", edytta)


print(girl_with_mandolin)
veneer = Marketplace()
veneer.show_listings()
veneer.add_listing(girl_with_mandolin)
veneer.show_listings()

edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")
veneer.show_listings()















