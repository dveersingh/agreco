from flask_app import db,ma



farmer_identifier = db.Table('farmer_identifier',
    db.Column('fpo_id', db.Integer, db.ForeignKey('fpo.FPO_ID')),
    db.Column('farmer_id', db.Integer, db.ForeignKey('farmer.AE_Farmer_ID'))
)

class Farmer(db.Model):
	__tablename__ = 'farmer'
	AE_Farmer_ID = db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(100))
	Father_Name = db.Column(db.String(100))
	National_ID = db.Column(db.String(100),unique=True)
	#FPO_ID = db.Column(db.String(100))
	Kissan_Card = db.Column(db.String(100),unique=True)
	Farm_ID = db.Column(db.String(100),unique=True)
	Level_of_Education = db.Column(db.String(100))
	Language = db.Column(db.String(100))
	Geographic_Location = db.Column(db.String(100))
	Annual_Income = db.Column(db.String(100))
	no_of_Crops_in_a_year = db.Column(db.Integer)#number
	no_of_farm_assets = db.Column(db.String(100))
	Land_holding_Area = db.Column(db.String(100))
	Land_holding_for_cultivation_Area_ = db.Column(db.String(100))
	Mobile_Number = db.Column(db.Integer,unique=True, nullable=False)#number
	Photograph = db.Column(db.String(100))
	Address = db.Column(db.String(100))
	Tehasil = db.Column(db.String(100))
	Pincode = db.Column(db.Integer)#number
	Aadhar_Card_No = db.Column(db.Integer,unique=True)#number
	Soil_Health_Card = db.Column(db.String(100))
	KVK_associated_with = db.Column(db.String(100))
	Panchayat_Associated_with = db.Column(db.String(100))
	Village = db.Column(db.String(100))
	email = db.Column(db.String(120),unique=True, nullable=False)
	fpos = db.relationship("FPO",
                               secondary=farmer_identifier,backref="farmers",lazy="dynamic")

	
		
class FPO(db.Model):
	
	__tablename__ = 'fpo'
	FPO_ID = db.Column(db.Integer, primary_key=True)
	Geographic_Location = db.Column(db.String(100))
	Rgisterd_as_a_Company = db.Column(db.String(100))
	Annual_Rvenue = db.Column(db.String(100))
	No_of_Farmers = db.Column(db.Integer)#number
	Total_Acreage = db.Column(db.String(100))
	Cultivable_Acreage_Season_wise = db.Column(db.String(100))
	CBBO_associated_with = db.Column(db.String(100))
	Number_of_Services = db.Column(db.Integer)#number
	Type_of_services = db.Column(db.String(100))
	FPO_Assets = db.Column(db.String(100))
	No_of_Partnerships = db.Column(db.Integer)#number
	Types_of_Partnerships = db.Column(db.String(100))
	Name_of_partners = db.Column(db.String(100))
	Licenses = db.Column(db.String(100))
	Certifications = db.Column(db.String(100))
	Logo = db.Column(db.String(100))
	PAN = db.Column(db.String(100),unique=True, nullable=False)
	Mobile_No = db.Column(db.Integer,unique=True, nullable=False)#number
	#farmer_ = db.relationship("Farmer",
     #                          secondary=farmer_identifier,backref="fpos")


	
	
class FarmerSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = Farmer
class FPOSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = FPO
		
farmer_schema = FarmerSchema()
farmers_schema = FarmerSchema(many=True)

fpo_schema = FPOSchema()
fpos_schema = FPOSchema(many=True)

def create_farmer(
					FPO_ID,
					Name , 
					Language, 	
					Father_Name ,
					National_ID ,
					Kissan_Card , 
					Farm_ID ,
					Level_of_Education , 
					Geographic_Location ,
					Annual_Income , 
					no_of_Crops_in_a_year,
					no_of_farm_assets , 
					Land_holding_Area ,
					Land_holding_for_cultivation_Area_ , 
					Mobile_Number ,	
					Photograph , 
					Address,
					Tehasil, 
					Pincode, 
					Aadhar_Card_No , 
					Soil_Health_Card , 
					KVK_associated_with ,
					Panchayat_Associated_with, 
					Village , 
					email 
				):
 
	farmer_c =  Farmer(	Name = Name, 
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
	db.session.add(farmer_c)
	db.session.commit()
	fpo_to_add = FPO.query.filter_by(FPO_ID = FPO_ID).first()
	farmer_c.fpos.append(fpo_to_add)
	db.session.commit()
	farmer_count  = db.session.query(Farmer).join(Farmer.fpos).filter(FPO.FPO_ID==FPO_ID).count()
	update_no_of_farmers = db.session.query(FPO).filter(FPO.FPO_ID == FPO_ID).one()
	update_no_of_farmers.No_of_Farmers = farmer_count
	db.session.commit()

	return farmer_c
	
	
def create_fpo(
				Geographic_Location ,
				Rgisterd_as_a_Company ,
				Annual_Rvenue ,
				Total_Acreage , 
				Cultivable_Acreage_Season_wise , 
				CBBO_associated_with ,
				Number_of_Services ,
				Type_of_services ,
				FPO_Assets,
				No_of_Partnerships ,
				Types_of_Partnerships ,
				Name_of_partners ,
				Licenses ,
				Certifications ,
				Logo ,
				PAN ,
				Mobile_No 
			):
			
			
	data = FPO(	Geographic_Location = Geographic_Location,
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

	db.session.add(data)
	
	db.session.commit()
	return data
 
def update_farmer(farmer_id, new_fpo_id):
	fpo_to_add = FPO.query.filter_by(FPO_ID = new_fpo_id).first()
	farmer_to_add = Farmer.query.filter_by(AE_Farmer_ID = farmer_id).first()
	farmer_to_add.fpos.append(fpo_to_add)
	db.session.commit()
	farmer_count  = db.session.query(Farmer).join(Farmer.fpos).filter(FPO.FPO_ID==new_fpo_id).count()
	update_no_of_farmers = db.session.query(FPO).filter(FPO.FPO_ID == new_fpo_id).one()
	update_no_of_farmers.No_of_Farmers = farmer_count
	db.session.commit()
	return farmer_to_add
	
if __name__ == "__main__":

    # Run this file directly to create the database tables.
    
    db.create_all()
    print("Done!")

