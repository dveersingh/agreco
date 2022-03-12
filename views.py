import os
import uuid



from flask_app import app

from flask import request, jsonify,render_template,flash, redirect

from models import db,Farmer, FPO, create_farmer, create_fpo, update_farmer, farmer_identifier
@app.route('/')
def indext():
    
    return render_template('index.html')




@app.route('/farmers_list')
def farmers_list():
    farmers = Farmer.query.all()
    return render_template('farmers_list.html', farmers=farmers)


@app.route('/farmer_full_detail/<ID>')
def farmer_full_detail(ID):
    farmers = Farmer.query.filter_by(AE_Farmer_ID = ID)
    return render_template('farmer_full_detail_list.html',farmers = farmers)


@app.route('/fpo_list')
def fpo_list():
    fpos = FPO.query.all()
    return render_template('fpo_list.html', fpos=fpos)


@app.route('/farmer_form')
def farmer_form_render():
	return render_template('farmerDetailsForm.html')
	
@app.route('/farmer_update_form')
def farmer_update_form():
	return render_template('farmerUpdateForm.html')
	
@app.route('/fpo_form')
def fpo_form_render():
	return render_template('fpoDetailsForm.html')


@app.route('/farmer_form', methods=['POST'])
def farmer_form_post():

	if request.method == 'POST':
		file1 = request.files['file1']
		filename, file_extension = os.path.splitext(file1.filename)
		unique_id = str(uuid.uuid4()) # genrating id
		Photo = os.path.join(app.config['UPLOAD_FOLDER'], unique_id+file_extension)
		Photograph= unique_id+file_extension
		file1.save(Photo) # saving file
		
		
		Name = request.form.get('Name',"")
		Language = request.form.get('Language',"")
		Father_Name = request.form.get('Father_Name',"")
		National_ID = request.form.get('National_ID',"")
		FPO_ID = request.form.get('FPO_ID',"")
		Kissan_Card = request.form.get('Kissan_Card',"")
		Farm_ID = request.form.get('Farm_ID',"")
		Level_of_Education = request.form.get('Level_of_Education',"")
		Geographic_Location = request.form.get('Geographic_Location',"")
		Annual_Income = request.form.get('Annual_Income',"")
		no_of_Crops_in_a_year = request.form.get('no_of_Crops_in_a_year',"")
		no_of_farm_assets  = request.form.get('no_of_farm_assets',"")
		Land_holding_Area = request.form.get('Land_holding_Area',"")
		Land_holding_for_cultivation_Area_ = request.form.get('Land_holding_for_cultivation_Area_',"")
		Mobile_Number	 = request.form.get('Mobile_Number',"")
		#Photograph  = request.form.get('Photograph',"")
		Address = request.form.get('Address',"")
		Tehasil  = request.form.get('Tehasil',"")
		Pincode = request.form.get('Pincode',"")
		Aadhar_Card_No = request.form.get('Aadhar_Card_No',"")
		Soil_Health_Card = request.form.get('Soil_Health_Card',"")
		KVK_associated_with = request.form.get('KVK_associated_with',"")
		Panchayat_Associated_with  = request.form.get('Panchayat_Associated_with',"")
		Village = request.form.get('Village',"")
		email = request.form.get('email',"")
		exist = bool(db.session.query(Farmer).filter_by(email=email,
			National_ID=National_ID,Kissan_Card =Kissan_Card,
			Mobile_Number = Mobile_Number, Farm_ID = Farm_ID,
			Aadhar_Card_No = Aadhar_Card_No).first())
		if exist:
			flash('Farmer exist in the Database')
			return render_template('farmerDetailsForm.html')
		
		farmer_data = create_farmer(
						FPO_ID = FPO_ID,
						Name = Name, 
						Language = Language, 	
						Father_Name = Father_Name,
						National_ID = National_ID,
						Kissan_Card = Kissan_Card, 
						Farm_ID = Farm_ID,
						Level_of_Education = Level_of_Education, 
						Geographic_Location = Geographic_Location,
						Annual_Income = Annual_Income, 
						no_of_Crops_in_a_year = no_of_Crops_in_a_year,
						no_of_farm_assets = no_of_farm_assets, 
						Land_holding_Area = Land_holding_Area,
						Land_holding_for_cultivation_Area_ = Land_holding_for_cultivation_Area_, 
						Mobile_Number = Mobile_Number,	
						Photograph = Photograph, 
						Address = Address,
						Tehasil = Tehasil, 
						Pincode = Pincode, 
						Aadhar_Card_No = Aadhar_Card_No, 
						Soil_Health_Card = Soil_Health_Card, 
						KVK_associated_with = KVK_associated_with,
						Panchayat_Associated_with = Panchayat_Associated_with, 
						Village = Village, 
						email = email
					)
		flash('DATA ADDED TO THE DATABASE')
		return render_template('farmerDetailsForm.html')
		


@app.route('/farmer_update_form',methods=['GET', 'POST'])
def farmer_update_form_post():
	if request.method == 'POST':
		farmer_id = request.form.get('farmer_id',"")
		new_fpo_id = request.form.get('new_fpo_id',"")
		exist_farmer = bool(db.session.query(Farmer).filter_by(AE_Farmer_ID=farmer_id).first())
		if exist_farmer == False:
			flash("farmer does not exist in database")
			return render_template('farmerUpdateForm.html')
		exist_fpo = bool(db.session.query(FPO).filter_by(FPO_ID=new_fpo_id).first())
		if exist_fpo == False:
			flash("fpo does not exist in database")
			return render_template('farmerUpdateForm.html')
		checker = False
		farmers = db.session.query(Farmer).all()
		for farmer in farmers:
			for fpo in farmer.fpos:
				if farmer.AE_Farmer_ID == int(farmer_id) and fpo.FPO_ID == int(new_fpo_id):
					flash("Can not add again, farmer already added to the fpo")
					return render_template('farmerUpdateForm.html')
					
			
			


		farmer_data = update_farmer(farmer_id, new_fpo_id)
		return render_template('farmerUpdateForm.html')

	
@app.route('/fpo_form', methods=['GET', 'POST'])
def fpo_form_post():

	if request.method == 'POST':
		file1 = request.files['file1']
		filename, file_extension = os.path.splitext(file1.filename)
		unique_id = str(uuid.uuid4()) # genrating id
		Logo = unique_id+file_extension
		L = os.path.join(app.config['UPLOAD_FOLDER'], unique_id+file_extension)
		file1.save(L) # saving file
		
		
		Geographic_Location =  request.form.get('Geographic_Location',"")
		Rgisterd_as_a_Company =  request.form.get('Rgisterd_as_a_Company',"")
		Annual_Rvenue =  request.form.get('Annual_Rvenue',"")
		Total_Acreage =  request.form.get('Total_Acreage',"")
		Cultivable_Acreage_Season_wise =  request.form.get('Cultivable_Acreage_Season_wise',"")
		CBBO_associated_with =  request.form.get('CBBO_associated_with',"")
		Number_of_Services =  request.form.get('Number_of_Services',"")
		Type_of_services =  request.form.get('Type_of_services',"")
		FPO_Assets =  request.form.get('FPO_Assets',"")
		No_of_Partnerships =  request.form.get('No_of_Partnerships',"")
		Types_of_Partnerships =  request.form.get('Types_of_Partnerships',"")
		Name_of_partners =  request.form.get('Name_of_partners',"")
		Licenses =  request.form.get('Licenses',"")
		Certifications  =  request.form.get('Certifications',"")
		#Logo =  request.form.get('Logo',"")
		PAN =  request.form.get('PAN',"")
		Mobile_No =  request.form.get('Mobile_No',"")
		exist = bool(db.session.query(FPO).filter_by(Mobile_No=Mobile_No ,PAN = PAN).first())
		if exist:
			flash('FPO ALREDY EXIST IN DATABASE')
			return render_template('fpoDetailsForm.html')
		
		fpo_data = create_fpo(	Geographic_Location = Geographic_Location,
					Rgisterd_as_a_Company = Rgisterd_as_a_Company,
					Annual_Rvenue = Annual_Rvenue,
					Total_Acreage = Total_Acreage, 
					Cultivable_Acreage_Season_wise = Cultivable_Acreage_Season_wise, 
					CBBO_associated_with = CBBO_associated_with,
					Number_of_Services = Number_of_Services,
					Type_of_services = Type_of_services,
					FPO_Assets = FPO_Assets,
					No_of_Partnerships = No_of_Partnerships,
					Types_of_Partnerships = Types_of_Partnerships,
					Name_of_partners = Name_of_partners,
					Licenses = Licenses,
					Certifications  = Certifications,
					Logo = Logo,
					PAN = PAN,
					Mobile_No = Mobile_No
					
				)
		flash('DATA ADDED TO THE DATABASE')

		return render_template('fpoDetailsForm.html')
		