from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/submit",methods=['POST'])
def sendData():
    if request.method == 'POST':
        #ต้นทุนวัตถุดิบs
        cost_price = request.form.getlist('cost_price', type=float)
        cost_amount = request.form.getlist('cost_amount', type=float)
        cost_used = request.form.getlist('cost_used', type=float)

        cost_total = 0.0
        for price, amount, used in zip(cost_price, cost_amount, cost_used):
            
            row_total = 0.0
            
            # ป้องกันการหารด้วย 0 (ZeroDivisionError)
            if amount > 0:
                # สูตรคำนวณต้นทุนของแถวนี้
                # (ราคา / ปริมาณทั้งหมด) * จำนวนที่ใช้
                row_total = (price / amount) * used
            
            # เพิ่มต้นทุนแถวนี้ เข้าไปในยอดรวมทั้งหมด
            cost_total += row_total

        #ค่าเสื่อม
        expenses = request.form.getlist('expenses', type=float)
        product_amount = request.form.getlist('product_amount', type=float)

        #บรรจุภัณฑ์
        package_price = request.form.getlist('package_price', type=float)
        package_amount = request.form.getlist('package_amount', type=float)

        #แรงงาน

        return render_template(
            'summary.html', 
            cost_total=cost_total
        )


if __name__ == "__main__":
    app.run(debug=True)

