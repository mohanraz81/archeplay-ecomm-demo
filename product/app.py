from flask import Flask, jsonify
from flask import request
import sys,os,boto3
from boto3 import session
import logging,json
import base64
import random,string
import hashlib,uuid,datetime
import decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)
    

app = Flask(__name__)
@app.route('/status', methods=['GET'])
def status():
    successmessage={"status": 200}
    return(successmessage)
@app.route('/api/v1.0/dumpproduct', methods=['GET'])
def dumpproduct():
  awsregion=os.environ['AWS_REGION']
  TableName=os.environ['TABLE_NAME']
  dynamodb=boto3.resource('dynamodb',region_name=awsregion)
  table=dynamodb.Table(TableName)
  items = [
      {
      "id": "skagen_skw6327",
      "title": "Skagen",
      "description": "Skagen Men's SKW6327 Hagen Stainless Steel Mesh Watch",
      "image": "skagen_skw6327.png",
      "Price": "100"
  },
  {
      "id": "skagen_titanium",
      "title": "Skagen",
      "description": "Skagen Connected Men's Holst Titanium Hybrid Smartwatch",
      "image": "skagen_titanium.png",
      "Price": "120"
  },
  {
      "id": "fossil_smartwatch_gen4",
      "title": "Fossil Smartwatch",
      "description": "Fossil Men's Gen 4 Explorist HR Stainless Steel Touchscreen Smartwatch with Heart Rate, GPS, NFC, and Smartphone Notifications",
      "image": "fossil_smartwatch_gen4.png",
      "Price": "100"
  },
  {
      "id": "fossil_nate_stainless",
      "title": "Fossil Nate Stainless",
      "description": "Fossil Men's Nate Stainless Steel Hybrid Smartwatch with Activity Tracking and Smartphone Notifications",
      "image": "fossil_nate_stainless.png",
      "Price": "110"
  },
  {
      "id": "apple_series5",
      "title": "Apple Series 5",
      "description": "Apple Watch Series 5 (GPS, 40mm) - Space Gray Aluminum Case with Black Sport Band",
      "image": "apple_series5.png",
      "Price": "130"
  },
  {
      "id": "samsung_smartwatch",
      "title": "Samsung smartwatch",
      "description": "Samsung Galaxy Smartwatch (46mm) Bluetooth - Silver/Black",
      "image": "samsung_smartwatch.png",
      "Price": "140"
  },
  {
      "id": "tagheuer_carrera",
      "title": "Tag Heuer",
      "description": "Mens Tag heuer Carrera Calibre Heuer 01 Automatic Chronograph 45 MM CAR2A1W.BA0703",
      "image": "tagheuer_carrera.png",
      "Price": "100"
  },
  {
      "id": "Casio_Analog",
      "title": "Casio",
      "description": "Casio Analog Black Dial Men's Watch-MTP-VT01L-1BUDF (A1615)",
      "image": "Casio Analog Black Dial Men's Watch-MTP-VT01L-1BUDF (A1615).PNG",
      "Price": "140"
  },
  {
      "id": "Casio_Enticer",
      "title": "Casio",
      "description": "Casio Enticer Analog Black Dial Men's Watch - MTP-VD01G-1BVUDF (A1367)",
      "image": "Casio Enticer Analog Black Dial Men's Watch - MTP-VD01G-1BVUDF (A1367).PNG",
      "Price": "200"
  },
  {
      "id": "Casio_Enticer_Analog",
      "title": "Casio",
      "description": "Casio Enticer Analog Blue Dial Men's Watch - MTP-1314D-2AVDF (A551)",
      "image": "Casio Enticer Analog Blue Dial Men's Watch - MTP-1314D-2AVDF (A551).PNG",
      "Price": "300"
  },
  {
      "id": "Casio_Enticer_Blue",
      "title": "Casio",
      "description": "Casio Enticer Analog Blue Dial Men's Watch - MTP-VD01D-2EVUDF (A1364)",
      "image": "Casio Enticer Analog Blue Dial Men's Watch - MTP-VD01D-2EVUDF (A1364).PNG",
      "Price": "250"
  },
  {
      "id": "Casio_Enticer_Silver",
      "title": "Casio",
      "description": "Casio Enticer Analog Silver Dial Men's Watch - MTP-V001D-7BUDF (A1082)",
      "image": "Casio Enticer Analog Silver Dial Men's Watch - MTP-V001D-7BUDF (A1082).PNG",
      "Price": "100"
  },
  {
      "id": "Casio_Chronograph",
      "title": "Casio",
      "description": "Casio Enticer Chronograph Black Dial Men's Watch - MTP-1374L-1AVDF (A834)",
      "image": "Casio Enticer Chronograph Black Dial Men's Watch - MTP-1374L-1AVDF (A834).PNG",
      "Price": "200"
  },
  {
      "id": "Casio_Youth_Combination",
      "title": "Casio",
      "description": "Casio Youth-Combination Analog-Digital Gold Dial Men's Watch - AEQ-110BW-9AVDF (AD206)",
      "image": "Casio Youth-Combination Analog-Digital Gold Dial Men's Watch - AEQ-110BW-9AVDF (AD206).PNG",
      "Price": "200"
  },
  {
      "id": "casio-MTP-v300D",
      "title": "Casio",
      "description": "casio-MTP-v300D-1AUDF(A1173)",
      "image": "casio-MTP-v300D-1AUDF(A1173).PNG",
      "Price": "200"
  },
  {
      "id": "casio-MTP-v300D-7AUDF",
      "title": "Casio",
      "description": "casio-MTP-v300D-7AUDF(A1177)",
      "image": "casio-MTP-v300D-7AUDF(A1177).PNG",
      "Price": "200"
  },
  {
      "id": "casio-MTP-vD01L-1EVUDF",
      "title": "Casio",
      "description": "casio-MTP-vD01L-1EVUDF",
      "image": "casio-MTP-vD01L-1EVUDF.PNG",
      "Price": "120"
  },
  {
      "id": "scuderia_ferrari",
      "title": "Scuderia Ferrari",
      "description": "Scuderia Ferrari Men's Stainless Steel Quartz Watch with Silicone Strap, Black, 24 (Model: 830344)",
      "image": "scuderia_ferrari.png",
      "Price": "100"
  },
  {
      "id": "armani_exchange",
      "title": "Armani Exchange",
      "description": "Armani Exchange Men's Classic Stainless Steel Watch",
      "image": "armani_exchange.png",
      "Price": "200"
  },
  {
      "id": "casio_vintage_a168wa",
      "title": "Casio Vintage",
      "description": "Casio Men's Vintage A168WA-1 Electro Luminescence Watch",
      "image": "casio_vintage_a168wa.png",
      "Price": "250"
  }
  ]
  for i in items:
      table.put_item(Item=i)
  successmessage={"status": 200,"statusmessage": "Added Items"}
  return(successmessage)

@app.route('/api/v1.0/getallproduct', methods=['GET'])
def getallproduct():
  awsregion=os.environ['AWS_REGION']
  TableName=os.environ['TABLE_NAME']
  dynamodb=boto3.resource('dynamodb',region_name=awsregion)
  table=dynamodb.Table(TableName)
  scan_kwargs = {
        "ProjectionExpression": "id, title, description, image, Price"
    }
  done = False
  start_key = None
  response = table.scan(**scan_kwargs)
  response=json.loads(json.dumps(response,cls=DecimalEncoder))
  successmessage={
      "status": 200,
      "statusmessage": "Added Items", 
      "response": response
  }
  return(successmessage)

@app.route('/api/v1.0/getproductbyid', methods=['POST'])
def getproductsbyid():
  awsregion=os.environ['AWS_REGION']
  TableName=os.environ['TABLE_NAME']
  dynamodb=boto3.resource('dynamodb',region_name=awsregion)
  table=dynamodb.Table(TableName)
  response = table.get_item(
    Key={
        'id': request.json['id']
    }
  )
  response=json.loads(json.dumps(response,cls=DecimalEncoder))
  successmessage={
      "status": 200,
      "statusmessage": "Added Items", 
      "response": response
  }
  return(successmessage)