def run_scraper():

  # Province and Municipality dict/list
  prov_and_muni_lists = {
    'Abra': [
      'Bangued', 'Boliney', 'Bucay', 'Bucloc', 'Daguioman', 'Danglas', 'Dolores (AA)', 'La Paz (AA)', 'Lacub', 'Lagangilang', 'Lagayan', 'Langiden', 'Licuan-Baay', 'Luba', 'Malibcong', 'Manabo', 'Penarrubia', 'Pidigan', 'Pilar (AA)', 'Sallapadan', 'San Isidro (AA)', 'San Juan (AA)', 'San Quintin (AA)', 'Tayum', 'Tineg', 'Tubo', 'Villaviciosa'
      ], 
    
    'Agusan del Norte': [
      'Buenavista (AN)', 'Carmen (AN)', 'Butuan', 'Cabadbaran', 'Jabonga', 'Kitcharao', 'Las Nieves', 'Magallanes (AN)', 'Nasipit', 'Remedios T. Romualdez', 'Santiago (AN)', 'Tubay'
      ], 
    
    'Agusan del Sur': [
      'Bunawan', 'Bayugan', 'Esperanza (AS)', 'La Paz (AS)', 'Loreto (AS)', 'Prosperidad', 'Rosario (AS)', 'San Francisco (AS)', 'San Luis (AS)', 'Santa Josefa', 'Sibagat', 'Talacogon', 'Trento', 'Veruela'
      ], 
    
    'Aklan': [
      'Altavas', 'Balete (AK)', 'Banga (AK)', 'Batan', 'Buruanga', 'Ibajay', 'Kalibo', 'Lezo', 'Libacao', 'Madalag', 'Makato', 'Malay', 'Malinao (AK)', 'Nabas', 'New Washington', 'Numancia', 'Tangalan'
      ], 
    
    'Albay': [
      'Bacacay', 'Camalig', 'Legazpi', 'Ligao', 'Tabaco', 'Daraga', 'Guinobatan', 'Jovellar', 'Libon', 'Malilipot', 'Malinao (AY)', 'Manito', 'Oas', 'Pio Duran', 'Polangui', 'Rapu-Rapu', 'Santo Domingo (AY)', 'Tiwi'
      ], 
    
    'Antique': [
      'Anini-Y', 'Barbaza', 'Belison', 'Bugasong', 'Caluya', 'Culasi', 'Hamtic', 'Laua-An', 'Libertad (AE)', 'Pandan (AE)', 'Patnongon', 'San Jose (AE)', 'San Remigio (AE)', 'Sebaste', 'Sibalom', 'Tibiao', 'Tobias Fornier', 'Valderrama'
      ], 
    
    'Apayao': [
      'Calanasan', 'Conner', 'Flora', 'Kabugao', 'Luna (AO)', 'Pudtol', 'Santa Marcela'
      ], 
    
    'Aurora': [
      'Baler', 'Casiguran (AU)', 'Dilasag', 'Dinalungan', 'Dingalan', 'Dipaculao', 'Maria Aurora', 'San Luis (AU)'
      ], 
    
    'Basilan': [
      'Akbar', 'Al-Barka', 'Isabela (BAS)', 'Lamitan', 'Hadji Mohammad Ajul', 'Hadji Muhtamad', 'Lantawan', 'Maluso', 'Sumisip', 'Tabuan-Lasa', 'Tipo-Tipo', 'Tuburan (BA)', 'Ungkaya Pukan'
      ], 
    
    'Bataan': [
      'Abucay', 'Bagac', 'Balanga', 'Dinalupihan', 'Hermosa', 'Limay', 'Mariveles', 'Morong (BN)', 'Orani', 'Orion', 'Pilar (BN)', 'Samal'
      ], 
      
    'Batanes': [
      'Basco', 'Itbayat', 'Ivana', 'Mahatao', 'Sabtang', 'Uyugan'
      ], 
    
    'Batangas': [
      'Agoncillo', 'Alitagtag', 'Balayan', 'Balete (BS)', 'Batangas', 'Bauan', 'Calaca', 'Calatagan', 'Lipa', 'Santo Tomas (BS)', 'Tanauan (BS)', 'Cuenca', 'Ibaan', 'Laurel', 'Lemery (BS)', 'Lian', 'Lobo', 'Mabini (BS)', 'Malvar', 'Mataasnakahoy', 'Nasugbu', 'Padre Garcia', 'Rosario (BS)', 'San Jose (BS)', 'San Juan (BS)', 'San Luis (BS)', 'San Nicolas (BS)', 'San Pascual (BS)', 'Santa Teresita (BS)', 'Taal', 'Talisay (BS)', 'Taysan', 'Tingloy', 'Tuy'
      ], 
    
    'Benguet': [
      'Atok', 'Bakun', 'Bokod', 'Buguias', 'Baguio', 'Itogon', 'Kabayan', 'Kapangan', 'Kibungan', 'La Trinidad', 'Mankayan', 'Sablan', 'Tuba', 'Tublay'
      ], 
      
      'Biliran': [
        'Almeria', 'Biliran', 'Cabucgayan', 'Caibiran', 'Culaba', 'Kawayan', 'Maripipi', 'Naval'
        ], 
    
    'Bohol': [
      'Alburquerque', 'Alicia (BL)', 'Anda (BL)', 'Antequera', 'Baclayon', 'Balilihan', 'Batuan (BL)', 'Bien Unido', 'Bilar', 'Buenavista (BL)', 'Calape', 'Candijay', 'Carmen (BL)', 'Catigbian', 'Tagbilaran', 'Clarin (BL)', 'Corella', 'Cortes (BL)', 'Dagohoy', 'Danao (BL)', 'Dauis', 'Dimiao', 'Duero', 'Garcia-Hernandez', 'Getafe', 'Guindulman', 'Inabanga', 'Jagna', 'Lila', 'Loay', 'Loboc', 'Loon', 'Mabini (BL)', 'Maribojoc', 'Panglao', 'Pilar (BL)', 'President Garcia', 'Sagbayan', 'San Isidro (BL)', 'San Miguel (BL)', 'Sevilla', 'Sierra Bullones', 'Sikatuna', 'Talibon', 'Trinidad', 'Tubigon', 'Ubay', 'Valencia (BL)'
      ], 
    
    'Bukidnon': [
      'Baungon', 'Cabanglasan', 'Malaybalay', 'Valencia (BK)', 'Damulog', 'Dangcagan', 'Don Carlos', 'Impasug-Ong', 'Kadingilan', 'Kalilangan', 'Kibawe', 'Kitaotao', 'Lantapan', 'Libona', 'Malitbog (BK)', 'Manolo Fortich', 'Maramag', 'Pangantucan', 'Quezon (BK)', 'San Fernando (BK)', 'Sumilao', 'Talakag'
      ], 
    
    'Bulacan': [
      'Angat', 'Balagtas', 'Baliwag', 'Bocaue', 'Bulakan', 'Bustos', 'Calumpit', 'Malolos', 'Meycauayan', 'Guiguinto (BU)', 'San Jose Del Monte', 'Dona Remedios Trinidad', 'Marilao', 'Hagonoy (BU)', 'Norzagaray', 'Obando', 'Pandi', 'Paombong', 'Plaridel (BU)', 'Pulilan', 'San Ildefonso (BU)', 'San Miguel (BU)', 'San Rafael (BU)', 'Santa Maria (BU)'
      ], 
    
    'Cagayan': [
      'Abulug', 'Alcala (CG)', 'Allacapan', 'Amulung', 'Aparri', 'Baggao', 'Ballesteros', 'Buguey', 'Calayan', 'Camalaniugan', 'Claveria (CG)', 'Enrile', 'Gattaran', 'Gonzaga', 'Iguig', 'Lallo', 'Lasam', 'Pamplona (CG)', 'Penablanca', 'Piat', 'Rizal (CG)', 'Sanchez-Mira', 'Santa Ana (CG)', 'Santa Praxedes', 'Santa Teresita (CG)', 'Santo Nino (CG)', 'Solana', 'Tuao', 'Tuguegarao'
      ], 
    
    'Camarines Norte': [
      'Basud (CN)', 'Capalonga', 'Daet', 'Jose Panganiban', 'Labo', 'Mercedes', 'Paracale', 'San Lorenzo Ruiz', 'San Vicente (CN)', 'Santa Elena', 'Talisay (CN)', 'Vinzons'
      ], 
    
    'Camarines Sur': [
      'Baao', 'Balatan', 'Bato (CS)', 'Bombon', 'Buhi', 'Bula', 'Cabusao', 'Calabanga', 'Camaligan', 'Canaman', 'Caramoan', 'Iriga', 'Naga (CS)', 'Del Gallego', 'Gainza', 'Garchitorena', 'Goa', 'Lagonoy', 'Libmanan', 'Lupi', 'Magarao', 'Milaor', 'Minalabac', 'Nabua', 'Ocampo', 'Pamplona (CS)', 'Pasacao', 'Pili', 'Presentacion', 'Ragay', 'Sagnay', 'San Fernando (CS)', 'San Jose (CS)', 'Sipocot', 'Siruma', 'Tigaon', 'Tinambac'
      ], 
    
    'Camiguin': [
      'Catarman (CM)', 'Guinsiliban', 'Mahinog', 'Mambajao', 'Sagay (CM)'
      ], 
    
    'Capiz': [
      'Roxas (CZ)', 'Cuartero', 'Dao', 'Dumalag', 'Dumarao', 'Ivisan', 'Jamindan', 'Ma-Ayon', 'Mambusao', 'Panay', 'Panitan', 'Pilar (CZ)', 'Pontevedra (CZ)', 'President Roxas (CZ)', 'Sapi-An', 'Sigma', 'Tapaz'
      ], 
    
    'Catanduanes': [
      'Bagamanoc', 'Baras (CT)', 'Bato (CT)', 'Caramoran', 'Gigmoto', 'Pandan (CT)', 'Panganiban', 'San Andres (CT)', 'San Miguel (CT)', 'Viga', 'Virac'
      ], 
      
    'Cavite': [
      'Alfonso', 'Amadeo', 'Carmona', 'Bacoor', 'Cavite', 'Dasmarinas', 'General Trias', 'Imus', 'Tagaytay', 'Trece Martires', 'Gen. Mariano Alvarez', 'Gen. Emilio Aguinaldo', 'Indang', 'Kawit', 'Magallanes (CE)', 'Maragondon', 'Mendez', 'Naic', 'Noveleta', 'Rosario (CE)', 'Silang', 'Tanza', 'Ternate'
      ], 
    
    'Cebu': [
      'Alcantara (CU)', 'Alcoy', 'Alegria (CU)', 'Aloguinsan', 'Argao', 'Asturias', 'Badian', 'Balamban', 'Bantayan Island', 'Barili', 'Boljoon', 'Borbon', 'Carmen (CU)', 'Catmon', 'Bogo', 'Carcar', 'Cebu', 'Danao (CU)', 'Lapu Lapu', 'Mandaue', 'Naga (CU)', 
      'Talisay  (CU)', 'Toledo', 'Compostela (CU)', 'Consolacion', 'Cordova', 'Daan Bantayan', 'Dalaguete', 'Dumanjug', 'Ginatilan', 'Liloan (CU)', 'Madridejos', 'Malabuyoc', 'Medellin', 'Minglanilla', 'Moalboal', 'Oslob', 'Pilar (CU)', 'Pinamungajan', 'Poro', 'Ronda', 'Samboan', 'San Fernando (CU)', 'San Francisco (CU)', 'San Remigio (CU)', 'Santa Fe (CU)', 'Santander', 'Sibonga', 'Sogod (CU)', 'Tabogon', 'Tabuelan', 'Tuburan (CU)', 'Tudela (CU)'
      ], 
    
    'Cotabato (North Cotabato)': [
      'Alamada', 'Aleosan', 'Antipas', 'Arakan', 'Banisilan', 'Carmen (NC)', 'Kidapawan', 'Kabacan', 'Libungan', 'Magpet', 'Makilala', 'Matalam', 'Midsayap', 'Mlang', 'Pigcawayan', 'Pikit', 'President Roxas (NC)', 'Tulunan'
      ], 
    
    'Davao De Oro': [
      'Compostela (DDO)', 'Laak', 'Mabini (CV)', 'Maco', 'Maragusan', 'Mawab', 'Monkayo', 'Montevista', 'Nabunturan', 'New Bataan', 'Pantukan'
      ], 
      
    'Davao Occidental': [
      'Don Marcelino', 'Jose Abad Santos', 'Malita', 'Sarangani', 'Santa Maria (DS)'
      ], 
    
    'Davao Oriental': [
      'Baganga', 'Banaybanay', 'Boston', 'Caraga', 'Cateel', 'Mati', 'Governor Generoso', 'Lupon', 'Manay', 'San Isidro (DO)', 'Tarragona'
      ], 
    
    'Davao del Norte': [
      'Asuncion', 'Braulio E. Dujali', 'Carmen (DN)', 'Panabo', 'Tagum', 'Igacos', 'Kapalong', 'New Corella', 'San Isidro (DN)', 'Santo Tomas (DN)', 'Talaingod'
      ], 
    
    'Davao del Sur': [
      'Bansalan', 'Davao', 'Digos', 'Hagonoy (DS)', 'Kiblawan', 'Magsaysay (DS)', 'Malalag', 'Matanao', 'Padada', 'Santa Cruz (DS)', 'Sulop'
      ], 
      
    'Dinagat Islands': [
      'Basilisa', 'Cagdianao', 'Dinagat', 'Libjo', 'Loreto (DI)', 'San Jose (DI)', 'Tubajon'
      ], 
    
    'Eastern Samar': [
      'Arteche', 'Balangiga', 'Balangkayan', 'Can-Avid', 'Borongan', 'Dolores (ES)', 'General Macarthur', 'Giporlos', 'Guiuan', 'Hernani', 'Jipapad', 'Lawaan', 'Llorente', 'Maslog', 'Maydolong', 'Mercedes (ES)', 'Oras', 'Quinapondan', 'Salcedo (ES)', 'San Julian', 'San Policarpo', 'Sulat', 'Taft'
      ], 
    
    'Guimaras': [
      'Buenavista (GS)', 'Jordan', 'Nueva Valencia', 'San Lorenzo', 'Sibunag'
      ], 
      
    'Ifugao': ['Aguinaldo', 'Alfonso Lista', 'Asipulo', 'Banaue', 'Hingyon', 'Hungduan', 'Kiangan', 'Lagawe', 'Lamut', 'Mayoyao', 'Tinoc'
      ], 
    
    'Ilocos Norte': [
      'Adams', 'Bacarra', 'Badoc', 'Bangui', 'Banna', 'Burgos (IN)', 'Carasi', 'Batac', 'Laoag', 'Currimao', 'Dingras', 'Dumalneg', 'Marcos', 'Nueva Era', 'Pagudpud', 'Paoay', 'Pasuquin', 'Piddig', 'Pinili', 'San Nicolas (IN)', 'Sarrat', 'Solsona', 'Vintar'
      ], 
    
    'Ilocos Sur': [
      'Alilem', 'Banayoyo', 'Bantay', 'Burgos (IS)', 'Cabugao', 'Caoayan', 'Cervantes', 'Candon', 'Vigan', 'Galimuyod', 'Gregorio Del Pilar', 'Lidlidda', 'Magsingal', 'Nagbukel', 'Narvacan', 'Quirino (IS)', 'Salcedo (IS)', 'San Emilio', 'San Esteban', 'San Ildefonso (IS)', 'San Juan (IS)', 'San Vicente (IS)', 'Santa', 'Santa Catalina (IS)', 'Santa Cruz (IS)', 'Santa Lucia', 'Santa Maria (IS)', 'Santiago (IS)', 'Santo Domingo (IS)', 'Sigay', 'Sinait', 'Sugpon', 'Suyo', 'Tagudin'
      ], 
    
    'Iloilo': [
      'Ajuy', 'Alimodian', 'Anilao', 'Badiangan', 'Balasan', 'Banate', 'Barotac Nuevo', 'Barotac Viejo', 'Batad', 'Bingawan', 'Cabatuan (IO)', 'Calinog', 'Carles', 'Iloilo', 'Passi', 'Concepcion (IO)', 'Dingle', 'Duenas', 'Dumangas', 'Estancia', 'Guimbal', 'Igbaras', 'Janiuay', 'Lambunao', 'Leganes', 'Lemery (IO)', 'Leon', 'Maasin (IO)', 'Miag-ao', 'Mina', 'New Lucena', 'Oton', 'Pavia', 'Pototan', 'San Dionisio', 'San Enrique (IO)', 'San Joaquin', 'San Miguel (IO)', 'San Rafael (IO)', 'Santa Barbara (IO)', 'Sara', 'Tigbauan', 'Tubungan', 'Zarraga'
      ], 
    
    'Isabela': [
      'Alicia (IA)', 'Angadanan', 'Aurora (IA)', 'Benito Soliven', 'Burgos (IA)', 'Cabagan', 'Cabatuan (IA)', 'Cauayan (IA)', 'Ilagan', 'Santiago (IA)', 'Cordon', 'Delfin Albano', 'Dinapigue', 'Divilacan', 'Echague', 'Gamu', 'Jones', 'Luna (IA)', 'Maconacon', 'Mallig', 'Naguilian (IA)', 'Palanan', 'Quezon (IA)', 'Quirino (IA)', 'Ramon', 'Reina Mercedes', 'Roxas (IA)', 'San Agustin (IA)', 'San Guillermo', 'San Isidro (IA)', 'San Manuel (IA)', 'San Mariano', 'San Mateo (IA)', 'San Pablo (IA)', 'Santa Maria (IA)', 'Santo Tomas (IA)', 'Tumauini'
      ], 
    
    'Kalinga': [
      'Balbalan', 'Tabuk', 'Lubuagan', 'Pasil', 'Pinukpuk', 'Rizal (KA)', 'Tanudan', 'Tinglayan'
      ], 
    
    'La Union': [
      'Agoo', 'Aringay', 'Bacnotan', 'Bagulin', 'Balaoan', 'Bangar', 'Bauang', 'Burgos (LU)', 'Caba', 'San Fernando (LU)', 'Luna (LU)', 'Naguilian (LU)', 'Pugo', 'Rosario (LU)', 'San Gabriel', 'San Juan (LU)', 'Santo Tomas (LU)', 'Santol', 'Sudipen', 'Tubao'
      ], 
    
    'Laguna': [
      'Alaminos (LA)', 'Bay', 'Calauan', 'Cavinti', 'Binan', 'Cabuyao', 'Calamba (LA)', 'San Pablo (LA)', 'San Pedro', 'Santa Rosa (LA)', 'Famy', 'Kalayaan (LA)', 'Liliw', 'Los Banos', 'Luisiana', 'Lumban', 'Mabitac', 'Magdalena', 'Majayjay', 'Nagcarlan', 'Paete', 'Pagsanjan', 'Pakil', 'Pangil', 'Pila', 'Rizal (LA)', 'Santa Cruz (LA)', 'Santa Maria (LA)', 'Siniloan', 'Victoria (LA)'
      ], 
    
    'Lanao Del Sur': [
      'Amai Manabilang', 'Bacolod-Kalawi', 'Balabagan', 'Balindong', 'Bayang', 'Binidayan', 'Buadiposo-Buntong', 'Bubong', 'Butig', 'Calanogas', 'Marawi', 'Ditsaan-Ramain', 'Ganassi', 'Kapai', 'Kapatagan (LS)', 'Lumba-Bayabao', 'Lumbaca-Unayan', 'Lumbatan', 'Lumbayanague', 'Madalum', 'Madamba', 'Maguing', 'Malabang', 'Marantao', 'Marogong', 'Masiu', 'Mulondo', 'Pagayawan', 'Piagapo', 'Picong', 'Poona Bayabao', 'Pualas', 'Saguiaran', 'Sultan Dumalondong', 'Tagoloan II', 'Tamparan', 'Taraka', 'Tubaran', 'Tugaya', 'Wao'
      ], 
    
    'Lanao del Norte': [
      'Bacolod (LN)', 'Baloi', 'Baroy', 'Iligan', 'Kapatagan (LN)', 'Kauswagan', 'Kolambugan', 'Lala', 'Linamon', 'Magsaysay (LN)', 'Maigo', 'Matungao', 'Munai', 'Nunungan', 'Pantao Ragat', 'Pantar', 'Poona Piagapo', 'Salvador', 'Sapad', 'Sultan Naga Dimaporo', 'Tagoloan (LN)', 'Tangcal', 'Tubod (LN)'
      ], 
    
    'Leyte': [
      'Abuyog', 'Alang-Alang', 'Albuera', 'Babatngon', 'Barugo', 'Bato (LE)', 'Burauen', 'Calubian', 'Capoocan', 'Carigara', 'Baybay', 'Ormoc', 'Tacloban', 'Dagami', 'Dulag', 'Hilongos', 'Hindang', 'Inopacan', 'Isabel', 'Jaro', 'Javier', 'Julita', 'Kananga', 'La Paz (LE)', 'Leyte', 'Macarthur', 'Mahaplag', 'Matag-Ob', 'Matalom', 'Mayorga', 'Merida', 'Palo', 'Palompon', 'Pastrana', 'San Isidro (LE)', 'San Miguel (LE)', 'Santa Fe (LE)', 'Tabango', 'Tabontabon', 'Tanauan (LE)', 'Tolosa', 'Tunga', 'Villaba'
      ], 
    
    'Maguindanao Del Norte': [
      'Barira', 'Buldon', 'Datu Blah Sinsuat', 'Datu Odin Sinsuat', 'Kabuntalan', 'Matanog', 'Northern Kabuntalan', 'Sultan Kudarat', 'Sultan Mastura', 'Talitay', 'Upi', 'Cotabato', 'Parang (MA)'
      ], 
    
    'Maguindanao Del Sur': [
      'Ampatuan', 'Buluan', 'Datu Abdullah Sangki', 'Datu Anggal Midtimbang', 'Datu Hoffer Ampatuan', 'Datu Paglas', 'Datu Piang', 'Datu Salibo', 'Datu Saudi-Ampatuan', 'Datu Unsay', 'Gen S.K Pendatun', 'Guindulungan', 'Mamasapano', 'Mangudadatu', 'Pagagawan', 'Pagalungan', 'Paglat', 'Pandag', 'Rajah Buayan', 'Shariff Aguak', 'Shariff Saydona Mustapha', 'South Upi', 'Sultan Sa Barongis', 'Talayan'
      ],

      'Metro Manila': [
        'Caloocan', 'Las Pinas', 'Makati', 'Malabon', 'Mandaluyong', 'Manila', 'Marikina', 'Muntinlupa', 'Navotas', 'Paranaque', 'Pasig', 'San Juan (MM)', 'Taguig', 'Valenzuela', 'Pasay', 'Pateros', 'Quezon (MM)'
      ],
    
    'Marinduque': [
      'Boac', 'Buenavista (ME)', 'Gasan', 'Mogpog', 'Santa Cruz (ME)', 'Torrijos'
      ], 
    
    'Masbate': [
      'Aroroy', 'Baleno', 'Balud', 'Batuan (MS)', 'Cataingan', 'Cawayan', 'Masbate', 'Claveria (MS)', 'Dimasalang', 'Esperanza (MS)', 'Mandaon', 'Milagros', 'Mobo', 'Monreal', 'Palanas', 'Pio V Corpuz', 'Placer (MS)', 'San Fernando (MS)', 'San Jacinto (MS)', 'San Pascual (MS)', 'Uson'
      ], 
    
    'Misamis Occidental': [
      'Aloran', 'Baliangao', 'Bonifacio', 'Oroquieta', 'Ozamiz', 'Tangub', 'Calamba (MC)', 'Clarin (MC)', 'Concepcion', 'Don Victoriano Chiongbian', 'Jimenez', 'Lopez Jaena', 'Panaon', 'Plaridel (MC)', 'Sapang Dalaga', 'Sinacaban', 'Tudela (MC)'
      ], 
    
    'Misamis Oriental': [
      'Alubijid', 'Balingasag', 'Balingoan', 'Binuangan', 'Cagayan De Oro', 'El Salvador', 'Gingoog', 'Claveria (MO)', 'Gitagum', 'Initao', 'Jasaan', 'Kinoguitan', 'Lagonglong', 'Laguindingan', 'Libertad (MO)', 'Lugait', 'Magsaysay (MO)', 'Manticao', 'Medina', 'Naawan', 'Opol', 'Salay', 'Sugbongcogon', 'Tagoloan (MO)', 'Talisayan', 'Villanueva'
      ], 
    
    'Mountain Province': [
      'Barlig', 'Bauko', 'Besao', 'Bontoc (MP)', 'Natonin', 'Paracelis', 'Sabangan', 'Sadanga', 'Sagada', 'Tadian'
      ], 
    
    'Negros Occidental': [
      'Binalbagan', 'Calatrava (NO)', 'Candoni', 'Cauayan (NO)', 'Bacolod (NO)', 'Bago', 'Cadiz', 'Escalante', 'Himamaylan', 'Kabankalan', 'La Carlota', 'Sagay (NO)', 'San Carlos (NO)', 'Silay', 'Sipalay', 'Talisay (NO)', 'Victorias', 'E. B. Magalona', 'Hinigaran', 'Hinobaan', 'Ilog', 'Isabela (NO)', 'La Castellana', 'Manapla', 'Moises Padilla', 'Murcia', 'Pontevedra (NO)', 'Pulupandan', 'Salvador Benedicto', 'San Enrique (NO)', 'Toboso', 'Valladolid'
      ], 
    
    'Negros Oriental': [
      'Amlan', 'Ayungon', 'Bacong', 'Basay', 'Bindoy', 'Bais', 'Bayawan', 'Canlaon', 'Dumaguete', 'Guihulngan', 'Tanjay', 'Dauin', 'Jimalalud', 'La Libertad (NR)', 'Mabinay', 'Manjuyod', 'Pamplona (NR)', 'San Jose (NR)', 'Santa Catalina (NR)', 'Siaton', 'Sibulan', 'Tayasan', 'Valencia (NR)', 'Vallehermoso', 'Zamboanguita'
      ], 
    
    'Northern Samar': [
      'Allen', 'Biri', 'Bobon', 'Capul', 'Catarman (NS)', 'Catubig', 'Gamay', 'Laoang', 'Lapinig', 'Las Navas', 'Lavezares', 'Lope De Vega', 'Mapanas', 'Mondragon', 'Palapag', 'Pambujan', 'Rosario (NS)', 'San Antonio (NS)', 'San Isidro (NS)', 'San Jose (NS)', 'San Roque', 'San Vicente (NS)', 'Silvino Lobos', 'Victoria (NS)'
      ], 
    
    'Nueva Ecija': [
      'Aliaga', 'Bongabon', 'Cabiao', 'Carranglan', 'Cabanatuan', 'Gapan', 'Palayan', 'Cuyapo', 'Gabaldon', 'General Mamerto Natividad', 'General Tinio', 'Guimba', 'Jaen', 'Laur', 'Licab', 'Llanera', 'Lupao', 'Nampicuan', 'Pantabangan', 'Penaranda', 'Quezon (NE)', 'Rizal (NE)', 'San Antonio (NE)', 'San Isidro (NE)', 'San Jose (NE)', 'San Leonardo', 'Santa Rosa (NE)', 'Santo Domingo (NE)', 'Science City of Munoz', 'Talavera', 'Talugtug', 'Zaragoza'
      ], 
    
    'Nueva Vizcaya': [
      'Alfonso Castaneda', 'Ambaguio', 'Aritao', 'Bagabag', 'Bambang', 'Bayombong', 'Diadi', 'Dupax Del Norte', 'Dupax Del Sur', 'Kasibu', 'Kayapa', 'Quezon (NV)', 'Santa Fe (NV)', 'Solano', 'Villaverde'
      ], 
    
    'Occidental Mindoro': [
      'Abra De Ilog', 'Calintaan', 'Looc (OM)', 'Lubang', 'Magsaysay (OM)', 'Mamburao', 'Paluan', 'Rizal (OM)', 'Sablayan', 'San Jose (OM)', 'Santa Cruz (OM)'
      ], 
    
    'Oriental Mindoro': [
      'Baco', 'Bansud', 'Bongabong', 'Bulalacao', 'Calapan', 'Gloria', 'Mansalay', 'Naujan', 'Pinamalayan', 'Pola', 'Puerto Galera', 'Roxas (OR)', 'San Teodoro', 'Socorro (OR)', 'Victoria (OR)'
      ], 
    
    'Palawan': [
      'Aborlan', 'Agutaya', 'Araceli', 'Balabac', 'Bataraza', 'Busuanga', 'Cagayancillo', 'Puerto Princesa', 'Coron', 'Culion', 'Cuyo', 'Dumaran', 'El Nido', 'Kalayaan (PN)', 'Linapacan', 'Magsaysay (PN)', 'Narra', 'Quezon (PN)', 'Rizal (PN)', 'Roxas (PN)', 'San Vicente (PN)', 'Sofronio Espanola', 'Taytay (PN)'
      ], 
    
    'Pampanga': [
      'Apalit', 'Arayat', 'Bacolor', 'Candaba', 'Angeles', 'San Fernando (PA)', 'Floridablanca', 'Guagua', 'Lubao', 'Mabalacat', 'Macabebe', 'Magalang', 'Masantol', 'Mexico', 'Minalin', 'Porac', 'San Luis (PA)', 'San Simon', 'Santa Ana (PA)', 'Santa Rita (PA)', 'Santo Tomas (PA)', 'Sasmuan'
      ], 
    
    'Pangasinan': [
      'Agno', 'Aguilar', 'Alcala (PS)', 'Anda (PS)', 'Asingan', 'Balungao', 'Bani', 'Basista', 'Bautista', 'Bayambang', 'Binalonan', 'Binmaley', 'Bolinao', 'Bugallon', 'Burgos (PS)', 'Calasiao', 'Alaminos (PS)', 'Dagupan', 'San Carlos (PS)', 'Urdaneta', 'Dasol', 'Infanta (PS)', 'Labrador', 'Laoac', 'Lingayen', 'Mabini (PS)', 'Malasiqui', 'Manaoag', 'Mangaldan', 'Mangatarem', 'Mapandan', 'Natividad', 'Pozorrubio', 'Rosales', 'San Fabian', 'San Jacinto (PS)', 'San Manuel (PS)', 'San Nicolas (PS)', 'San Quintin (PS)', 'Santa Barbara (PS)', 'Santa Maria (PS)', 'Santo Tomas (PS)', 'Sison (PS)', 'Sual', 'Tayug', 'Umingan', 'Urbiztondo', 'Villasis'
      ], 
    
    'Quezon': [
      'Agdangan', 'Alabat', 'Atimonan', 'Buenavista (QN)', 'Burdeos', 'Calauag', 'Candelaria (QN)', 'Catanauan', 'Lucena', 'Tayabas', 'Dolores (QN)', 'General Luna (QN)', 'General Nakar', 'Guinayangan', 'Gumaca', 'Infanta (QN)', 'Jomalig', 'Lopez', 'Lucban', 'Macalelon', 'Mauban', 'Mulanay', 'Padre Burgos (QN)', 'Pagbilao', 'Panukulan', 'Patnanungan', 'Perez', 'Pitogo (QN)', 'Plaridel (QN)', 'Polillo', 'Quezon (QN)', 'Real', 'Sampaloc', 'San Andres (QN)', 'San Antonio (QN)', 'San Francisco (QN)', 'San Narciso (QN)', 'Sariaya', 'Tagkawayan', 'Tiaong', 'Unisan'
      ], 
    
    'Quirino': [
      'Aglipay', 'Cabarroguis', 'Diffun', 'Maddela', 'Nagtipunan', 'Saguday'
      ], 
    
    'Rizal': [
      'Angono', 'Baras (RL)', 'Binangonan', 'Cainta', 'Cardona', 'Antipolo', 'Jalajala', 'Morong (RL)', 'Pililla', 'Rodriguez', 'San Mateo (RL)', 'Tanay', 'Taytay (RL)', 'Teresa'
      ], 
    
    'Romblon': [
      'Alcantara (RN)', 'Banton', 'Cajidiocan', 'Calatrava (RN)', 'Concepcion (RN)', 'Corcuera', 'Ferrol', 'Looc (RN)', 'Magdiwang', 'Odiongan', 'Romblon', 'San Agustin (RN)', 'San Andres (RN)', 'San Fernando (RN)', 'San Jose (RN)', 'Santa Fe (RN)', 'Santa Maria (Imelda)'
      ], 
    
    'Samar (Western Samar)': [
      'Almagro', 'Basey', 'Calbiga', 'Calbayog', 'Catbalogan', 'Daram', 'Gandara', 'Hinabangan', 'Jiabong', 'Marabut', 'Matuguinao', 'Motiong', 'Pagsanghan', 'Paranas', 'Pinabacdao', 'San Jorge', 'San Jose De Buan', 'San Sebastian', 'Santa Margarita', 'Santa Rita (WS)', 'Santo Nino (WS)', 'Tagapul-An', 'Talalora', 'Tarangnan', 'Villareal', 'Zumarraga'
      ], 
    
    'Sarangani': [
      'Alabel', 'Glan', 'Kiamba', 'Maasim', 'Maitum', 'Malapatan', 'Malungon'
      ], 
    
    'Siquijor': [
      'Enrique Villanueva', 'Larena', 'Lazi', 'Maria', 'San Juan (SR)', 'Siquijor'
      ], 
    
    'Sorsogon': [
      'Barcelona', 'Bulan', 'Bulusan', 'Casiguran (SO)', 'Castilla', 'Sorsogon', 'Donsol', 'Gubat', 'Irosin', 'Juban', 'Magallanes (SO)', 'Matnog', 'Pilar (SO)', 'Prieto Diaz', 'Santa Magdalena'
      ], 
    
    'South Cotabato': [
      'Banga (SC)', 'General Santos', 'Koronadal', 'Lake Sebu', 'Norala', 'Polomolok', 'Santo Nino (SC)', 'Surallah', 'Tampakan', 'Tantangan', 'Tupi'
      ], 
    
    'Southern Leyte': [
      'Anahawan', 'Bontoc (SL)', 'Maasin (SL)', 'Hinunangan', 'Hinundayan', 'Libagon', 'Liloan (SL)', 'Limasawa', 'Macrohon', 'Malitbog (SL)', 'Padre Burgos (SL)', 'Pintuyan', 'Saint Bernard', 'San Francisco (SL)', 'San Juan (SL)', 'San Ricardo', 'Silago', 'Sogod (SL)', 'Tomas Oppus'
      ], 
    
    'Sultan Kudarat': [
      'Bagumbayan', 'Tacurong', 'Columbio', 'Esperanza (SK)', 'Isulan', 'Kalamansig', 'Lambayong', 'Lebak', 'Lutayan', 'Palimbang', 'President Quirino', 'Senator Ninoy Aquino'
      ], 
    
    'Sulu': [
      'Hadji Panglima Tahil', 'Indanan', 'Jolo', 'Kalingalan Caluang', 'Lugus', 'Luuk', 'Maimbung', 'Old Panamao', 'Omar', 'Pandami', 'Panglima Estino', 'Pangutaran', 'Parang (SU)', 'Pata', 'Patikul', 'Siasi', 'Talipao', 'Tapul', 'Tongkil'
      ], 
    
    'Surigao del Norte': [
      'Alegria (SN)', 'Bacuag', 'Burgos (SN)', 'Surigao', 'Claver', 'Dapa', 'Del Carmen', 'General Luna  (SN)', 'Gigaquit', 'Mainit', 'Malimono', 'Pilar (SN)', 'Placer (SN)', 'San Benito', 'San Francisco (SN)', 'San Isidro (SN)', 'Santa Monica', 'Sison (SN)', 'Socorro (SN)', 'Tagana-An', 'Tubod (SN)'
      ], 
    
    'Surigao del Sur': [
      'Barobo', 'Bayabas', 'Cagwait', 'Cantilan', 'Carmen (SS)', 'Carrascal', 'Bislig', 'Tandag', 'Cortes (SS)', 'Hinatuan', 'Lanuza', 'Lianga', 'Lingig', 'Madrid', 'Marihatag', 'San Agustin (SS)', 'San Miguel (SS)', 'Tagbina', 'Tago'
      ], 
    
    'Tarlac': [
      'Anao', 'Bamban', 'Camiling', 'Capas', 'Tarlac', 'Concepcion (TC)', 'Gerona', 'La Paz (TC)', 'Mayantoc', 'Moncada', 'Paniqui', 'Pura', 'Ramos', 'San Clemente', 'San Jose (TC)', 'San Manuel (TC)', 'Santa Ignacia', 'Victoria (TC)'
      ], 
    
    'Tawi-Tawi': [
      'Bongao', 'Languyan', 'Mapun', 'Panglima Sugala', 'Sapa-Sapa', 'Sibutu', 'Simunul', 'Sitangkai', 'South Ubian', 'Tandubas', 'Turtle Islands'
      ], 
    
    'Zambales': [
      'Botolan', 'Cabangan', 'Candelaria (ZA)', 'Castillejos', 'Olongapo', 'Iba', 'Masinloc', 'Palauig', 'San Antonio (ZA)', 'San Felipe', 'San Marcelino', 'San Narciso (ZA)', 'Santa Cruz (ZA)', 'Subic'
      ], 
    
    'Zamboanga Sibugay': [
      'Alicia (ZS)', 'Buug', 'Diplahan', 'Imelda', 'Ipil', 'Kabasalan', 'Mabuhay', 'Malangas', 'Naga (ZS)', 'Olutanga', 'Payao', 'R.T. Lim', 'Siay', 'Talusan', 'Titay', 'Tungawan'
      ], 
    
    'Zamboanga del Norte': [
      'Bacungan Leon B. Postigo', 'Baliguian', 'Dapitan', 'Dipolog', 'Godod', 'Gutalac', 'Jose Dalman', 'Kalawit', 'Katipunan', 'La Libertad (ZN)', 'Labason', 'Liloy', 'Manukan', 'Mutia', 'Pinan', 'Polanco', 'Roxas (ZN)', 'Rizal (ZN)', 'Salug', 'Sergio Osmena', 'Siayan', 'Sibuco', 'Sibutad', 'Sindangan', 'Siocon', 'Sirawai', 'Tampilisan'
      ], 
    
    'Zamboanga del Sur': [
      'Aurora (ZR)', 'Bayog', 'Pagadian', 'Zamboanga', 'Dimataling', 'Dinas', 'Dumalinao', 'Dumingag', 'Guipos', 'Josefina', 'Kumalarang', 'Labangan', 'Lakewood', 'Lapuyan', 'Mahayag', 'Margosatubig', 'Midsalip', 'Molave', 'Pitogo (ZR)', 'Ramon Magsaysay', 'San Miguel (ZR)', 'San Pablo (ZR)', 'Sominot', 'Tabina', 'Tambulig', 'Tigbao', 'Tukuran', 'Vincenzo A Sagun'
      ]
    }

  # Uncheck previous year list (add year if necessary)
  years = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]

  # Uncheck Economic Dynamism tab list (those are codes for each checkboxes)
  economic_dynamisms = ["les", "leg", "sle", "scb", "job", "col", "cdb", "fd", "pro", "pbpo"]

  # Uncheck Infrastructure tab list (those are codes for each checkboxes)
  infrastructures = ["road", "dtp", "abu", "trans", "edu", "hea", "inv", "acc", "ict", "atm"]

  from playwright.sync_api import sync_playwright
  import csv
  import re

  with sync_playwright() as playwright:

    extracted_tables = [] # >> for count of extracted tables
    extracted_municipalities = [] # >> for count of municipalities

    # Looping through every province and its corresponding cities

    for province, municipalities in prov_and_muni_lists.items():
      # Opening new page and the website
      browser = playwright.chromium.launch(headless=True, slow_mo=20) #20
      context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        viewport={"width": 1280, "height": 720}
      )
      main_page = context.new_page()
      main_page.goto("https://cmci.dti.gov.ph/data-portal.php", wait_until='domcontentloaded', timeout=60000)

      # Uncheck previous years
      for year in years:
        year_checkbox = main_page.locator(f'label[for="checkbox-inl-{year}"]')
        year_checkbox.wait_for(state="visible", timeout=5000)
        year_checkbox.click(force=True)

      # Clicking the tab for Economic Dynamism
      econ_dyn_btn = main_page.get_by_role("button", name="ECONOMIC DYNAMISM")
      econ_dyn_btn.click()

      # Uncheck Economic Dynamism checkboxes
      for economic_dynamism in economic_dynamisms:
        econ_dyn_checkbox = main_page.locator(f'label[for={economic_dynamism}]')
        econ_dyn_checkbox.wait_for(state="visible")
        main_page.wait_for_load_state("domcontentloaded")
        econ_dyn_checkbox.click(force=True)

      # Clicking the tab for Infrastructure
      infras_btn = main_page.get_by_role("button", name="INFRASTRUCTURE")
      infras_btn.click()

      # Uncheck Infrastructure checkboxes
      for infrastructure in infrastructures:
          infras_checkbox = main_page.locator(f'label[for={infrastructure}]')
          infras_checkbox.wait_for(state="visible")
          main_page.wait_for_load_state("domcontentloaded")
          infras_checkbox.click(force=True)

      # Selecting Municipalities
      print(f"----{province}----".upper())

      

      for municipality in municipalities:
        # Open dropdown search
        main_page.locator("#select2-lgu-container").click()

        # Filling searchbox with municipalities
        search = main_page.locator("input.select2-search__field")
        search.wait_for(timeout=5000)
        search.fill(municipality)

        extracted_municipalities.append(municipality)

        # Wait for selection to show
        # result = main_page.locator("li.select2-results__option.select2-results__option--highlighted", has_text=municipality)
        # result.wait_for(state="visible", timeout=5000)

        dropdown_options = main_page.locator("li.select2-results__option")
        dropdown_options.first.wait_for(state="visible", timeout=5000)

        # Loop through to find exact match
        def normalize(text):
          return re.sub(r'\s+', ' ', text).strip()

        count = dropdown_options.count()
        for i in range(count):
            option = dropdown_options.nth(i)
            if normalize(option.inner_text()) == normalize(municipality):
              option.click()
              break

        # Select the corresponding value from selection
        # result.click()
        print(f"Selected: {municipality}")
      print("--------------------")

      # Clicking the process button and entering a new tab
      with main_page.expect_popup() as pop_up:
        process_btn = main_page.get_by_role("button", name="Process Selections")
        process_btn.click(force=True)
      
      new_tab = pop_up.value
      new_tab.wait_for_load_state(state='load')

      # Choose filter government units
      # Clicking the dropdown
      select_gov_units = new_tab.locator("#select2-render-type-container").first.click(force=True)

      # Filling the searchbox with government unit
      search_box = new_tab.locator("input.select2-search__field")
      search_box.wait_for(timeout=5000)
      search_box.fill("By Government Unit")

      # Selecting the government unit
      search_rslt = new_tab.locator("li.select2-results__option.select2-results__option", has_text="By Government Unit")
      search_rslt.wait_for(state="visible", timeout=5000)
      new_tab.wait_for_load_state("domcontentloaded")
      search_rslt.click()

      # This wait is for extracting the table
      new_tab.wait_for_load_state("domcontentloaded", timeout=5000)

      # Extracting Economic Dynamism & Infrastructure tables
      # Selecting Cities
      cities_name = new_tab.locator('h2')
      cities_count = cities_name.count()

      # Selecting Tables
      tables = new_tab.locator('table.table.table-hover.table-bordered')
      tables_count = tables.count()
      extracted_tables.append(tables_count)

      extracted_data = []

      for i in range(cities_count):
      # Get city name
        city_name = cities_name.nth(i).inner_text().strip()

        # Get the table
        table = tables.nth(i)

        print(f"Got the data for: {city_name}")

        # Extract table
        rows = table.locator('tr')
        row_count = rows.count()

        # Looping all the rows from the table
        for row in range(row_count):
          cells = rows.nth(row).locator('td')

          if cells.count() == 2:
            left_column = cells.nth(0).inner_text().strip()
            right_column = cells.nth(1).inner_text().strip()

            extracted_data.append([city_name, left_column, right_column])
      print("--------------------")
      # print(extracted_data)

      # Save the extracted data through csv file
      with open(f'C:/Users/Admin/Music/hotdiggydidog/coding/python/platformUpdateAutomation/cmci/cmciResults2025/{province}.csv', 'w', newline='', encoding='utf-8') as file:
          writer = csv.writer(file)
          writer.writerow(["MUNICIPALITY", "CLASS", "VALUE"])
          writer.writerows(extracted_data)

      # close context and browser
      context.close()
      browser. close()

  # Stats
  print(f"Cities Count: {len(extracted_municipalities)}\nTables Count: {len(extracted_tables)}")