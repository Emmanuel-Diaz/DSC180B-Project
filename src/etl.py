#EXTRACT (Scrape images)

class Scraper:

	site = ""
	num_images = 0

	def __init__(self):
		raise Exception("Please select a site and number of images.")

	def __init__(self, site, num_images):
		self.site = site
		self.num_images = num_images



class WW2DB:

	def __init__(self):
		pass


	"""
	Gets WW2 Images
	Returns: Dictionary with year as key, art data as values
	"""
	def scrape_ww2_images(num_images):
	    
	    images = defaultdict(list)
	    
	    ww2db_link = "https://ww2db.com/photo.php"
	    
	    #Get random collection of art_ids to label artwork
	    img_ids = random.sample(range(15000), 10000)
	    
	    next_link = ww2db_link
	    out = scrape_ww2db_page(next_link, img_ids)

	    #Iterate while output of scraping exists
	    while out:
	        out = scrape_ww2db_page(next_link, art_ids, num_images)
	        
	        ####
	        for key,value in out.items():
	            images[key].extend(value)
	            
	        #Get next page for scraping
	        next_link = ww2db_next_page(next_link)
	        if next_link == "":
	            break
	            
	    return images

	"""
	Scrapes WW2 photographs from ww2db
	Params: link - Page to scrape from
	        img_ids - list of ids to label artwork
	"""
	def scrape_ww2db_page(link, img_ids):
	    
	    #Get WW2 Webpage
	    result = requests.get(link)
	    
	    # if successful parse the download into a BeautifulSoup object, which allows easy manipulation 
	    if result.status_code == 200:
	        soup = BeautifulSoup(result.text, "html.parser")
	        
	    #Store image links and metadata
	    images = defaultdict(list)
	    random.shuffle(img_ids)

	    image_url = None

	    #TODO - Create custom scraping routine for page
	   
	            
        #Find width/height of image
        width_m = re.search('width=(\d+)', image_url)
        height_m = re.search('height=(\d+)', image_url)  
        width = width_m.group(1) if width_m else 0
        height = height_m.group(1) if height_m else 0

	    #Store this photo
	    images[year].append({"url":image_url, "written_desc":photo_desc, "year":year,"dimension":(width,height), "img_id":curr_id, "src_id":1})
	        
	    return images



class MilitaryAlbum:

	def __init__(self):
		pass

	"""
	Gets MilitaryAlbum Images
	Returns: Dictionary with year as key, art data as values
	"""
	def scrape_military_images(num_images):
	    
	    images = defaultdict(list)
	    
	    military_link = "http://waralbum.ru/catalog/"
	    
	    #Get random collection of art_ids to label artwork
	    img_ids = random.sample(range(15000), 10000)
	    
	    next_link = military_link
	    out = scrape_military_page(next_link, img_ids)

	    #Iterate while output of scraping exists
	    while out:
	        out = scrape_military_page(next_link, art_ids, num_images)
	        
	        ####
	        for key,value in out.items():
	            images[key].extend(value)
	            
	        #Get next page for scraping
	        next_link = military_next_page(next_link)
	        if next_link == "":
	            break
	            
	    return images

	"""
	Scrapes WW2 photographs from WarAlbum
	Params: link - Page to scrape from
	        img_ids - list of ids to label artwork
	"""
	def scrape_ww2db_page(link, img_ids):
	    
	    #Get WarAlbum Webpage
	    result = requests.get(link)
	    
	    # if successful parse the download into a BeautifulSoup object, which allows easy manipulation 
	    if result.status_code == 200:
	        soup = BeautifulSoup(result.text, "html.parser")
	        
	    #Store image links and metadata
	    images = defaultdict(list)
	    random.shuffle(img_ids)

	    image_url = None

	    #TODO - Create custom scraping routine for page
	   
	            
        #Find width/height of image
        width_m = re.search('width=(\d+)', image_url)
        height_m = re.search('height=(\d+)', image_url)  
        width = width_m.group(1) if width_m else 0
        height = height_m.group(1) if height_m else 0

	    #Store this photo
	    images[year].append({"url":image_url, "written_desc":photo_desc, "year":year,"dimension":(width,height), "img_id":curr_id, "src_id":1})
	        
	    return images




#TRANSFORM (Data Augmentation)
#LOAD (Save dataset)