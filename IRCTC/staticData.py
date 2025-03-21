# Set of major railway stations across different states in India
irctc_stations = {
    "New Delhi",
    "Mumbai Central",
    "Chennai Central",
    "Kolkata Howrah",
    "Bengaluru City",
    "Hyderabad Deccan",
    "Ahmedabad Junction",
    "Pune Junction",
    "Lucknow Charbagh",
    "Patna Junction",
    "Bhopal Junction",
    "Jaipur Junction",
    "Secunderabad Junction",
    "Chandigarh Junction",
    "Nagpur Junction",
    "Thiruvananthapuram Central",
    "Guwahati Junction",
    "Visakhapatnam Junction",
    "Madurai Junction",
    "Coimbatore Junction",
    "Varanasi Junction",
    "Kanpur Central",
    "Agra Cantt",
    "Surat Junction",
    "Ranchi Junction",
    "Raipur Junction",
    "Jammu Tawi",
    "Dehradun Junction",
    "Gorakhpur Junction",
    "Amritsar Junction",
    "Bhagalpur Junction",
    "Jodhpur Junction",
    "Udaipur City",
    "Kochi Ernakulam Junction",
    "Gaya Junction",
    "Mysuru Junction",
    "Shirdi Junction",
    "Ajmer Junction",
    "Haridwar Junction",
    "Bareilly Junction",
    "Vadodara Junction",
    "Dibrugarh Junction",
    "Silchar Junction",
    "Allahabad Junction",
    "Cuttack Junction",
    "Rourkela Junction",
    "Itarsi Junction",
    "Bilaspur Junction",
    "Tirupati Junction",
    "Kanyakumari Junction",
    "Rajkot Junction",
    "Dhanbad Junction"
}

# Tuple containing all stations
railway_stations = tuple(irctc_stations)

# Sample realistic distances (in km) between major railway stations
random_distances = [
    # Delhi - North, West, East, and South Routes
    ('New Delhi', 'Jaipur Junction', 288),
    ('New Delhi', 'Chandigarh Junction', 266),
    ('New Delhi', 'Lucknow Charbagh', 512),
    ('New Delhi', 'Kanpur Central', 440),
    ('New Delhi', 'Mumbai Central', 1386),
    ('New Delhi', 'Ahmedabad Junction', 934),
    
    # Routes from Ahmedabad
    ('Ahmedabad Junction', 'Vadodara Junction', 110),
    ('Ahmedabad Junction', 'Surat Junction', 263),
    ('Ahmedabad Junction', 'Mumbai Central', 491),
    ('Ahmedabad Junction', 'Jodhpur Junction', 458),
    ('Ahmedabad Junction', 'Udaipur City', 268),
    ('Ahmedabad Junction', 'Jaipur Junction', 673),
    ('Ahmedabad Junction', 'Chandigarh Junction', 1150),
    
    # Western and Southern Routes
    ('Mumbai Central', 'Surat Junction', 265),
    ('Mumbai Central', 'Pune Junction', 149),
    ('Mumbai Central', 'Bengaluru City', 984),
    ('Mumbai Central', 'Hyderabad Deccan', 790),
    ('Mumbai Central', 'Chennai Central', 1338),
    ('Mumbai Central', 'Goa Madgaon', 579),
    
    # Eastern India Connections
    ('Kolkata Howrah', 'Patna Junction', 532),
    ('Kolkata Howrah', 'Varanasi Junction', 681),
    ('Kolkata Howrah', 'Ranchi Junction', 416),
    ('Kolkata Howrah', 'Dhanbad Junction', 259),
    ('Kolkata Howrah', 'Cuttack Junction', 435),
    ('Kolkata Howrah', 'Bhubaneswar', 445),
    
    # South India Major Routes
    ('Bengaluru City', 'Hyderabad Deccan', 577),
    ('Bengaluru City', 'Chennai Central', 362),
    ('Bengaluru City', 'Mysuru Junction', 139),
    ('Bengaluru City', 'Coimbatore Junction', 330),
    ('Chennai Central', 'Madurai Junction', 495),
    ('Chennai Central', 'Tirupati Junction', 144),
    ('Thiruvananthapuram Central', 'Kochi Ernakulam Junction', 220),
    
    # Northeast India Routes
    ('Guwahati Junction', 'Dibrugarh Junction', 450),
    ('Guwahati Junction', 'Silchar Junction', 198),
    ('Guwahati Junction', 'Kolkata Howrah', 1015),
    
    # Central India Routes
    ('Nagpur Junction', 'Bhopal Junction', 354),
    ('Bhopal Junction', 'Itarsi Junction', 77),
    ('Itarsi Junction', 'Bilaspur Junction', 474),
    ('Raipur Junction', 'Bilaspur Junction', 111),
    ('Raipur Junction', 'Nagpur Junction', 283),
    
    # Jammu and Uttarakhand Routes
    ('Jammu Tawi', 'Amritsar Junction', 208),
    ('Jammu Tawi', 'New Delhi', 577),
    ('Dehradun Junction', 'Haridwar Junction', 52),
    ('Dehradun Junction', 'New Delhi', 315),
    ('Haridwar Junction', 'Bareilly Junction', 172),
    
    # Bihar and Uttar Pradesh Routes
    ('Patna Junction', 'Varanasi Junction', 237),
    ('Varanasi Junction', 'Gaya Junction', 258),
    ('Varanasi Junction', 'Allahabad Junction', 121),
    
    # Odisha and Jharkhand Routes
    ('Cuttack Junction', 'Rourkela Junction', 350),
    ('Dhanbad Junction', 'Ranchi Junction', 163),
    
    # Rajasthan Important Routes
    ('Jaipur Junction', 'Ajmer Junction', 131),
    ('Ajmer Junction', 'Jodhpur Junction', 212),
    ('Jodhpur Junction', 'Udaipur City', 249),
    
    # Gujarat Connections
    ('Rajkot Junction', 'Ahmedabad Junction', 216),
    ('Rajkot Junction', 'Surat Junction', 532),
    
    # Tamil Nadu and Kerala Routes
    ('Madurai Junction', 'Coimbatore Junction', 214),
    ('Kanyakumari Junction', 'Thiruvananthapuram Central', 90),
    
    # Short Distances for More Route Variability
    ('Pune Junction', 'Mumbai Central', 149),
    ('Lucknow Charbagh', 'Kanpur Central', 74),
    ('Bhopal Junction', 'Nagpur Junction', 354),
    ('Chandigarh Junction', 'Dehradun Junction', 167),
    ('Nagpur Junction', 'Raipur Junction', 283),
    ('Visakhapatnam Junction', 'Bhubaneswar', 445)
]
