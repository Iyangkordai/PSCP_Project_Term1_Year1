from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/submit",methods=['POST'])
def sendData():
    if request.method == 'POST':
        #ต้นทุนวัตถุดิบ
        cost_list = request.form.getlist('cost_list')
        cost_price = request.form.getlist('cost_price', type=float)
        cost_amount = request.form.getlist('cost_amount', type=float)
        cost_used = request.form.getlist('cost_used', type=float)

        grand_total = 0.0
        all_cost_details = []
        for name, price, amount, used in zip(cost_list, cost_price, cost_amount, cost_used):
            
            row_total = 0.0
            
            # ป้องกันการหารด้วย 0 (ZeroDivisionError)
            if amount > 0:
                # สูตรคำนวณต้นทุนของแถวนี้
                # (ราคา / ปริมาณทั้งหมด) * จำนวนที่ใช้
                row_total = (price / amount) * used
            
            # เพิ่มต้นทุนแถวนี้ เข้าไปในยอดรวมทั้งหมด
            grand_total += row_total
            all_cost_details.append({
                'name': name,
                'price': price,
                'amount': amount,
                'used': used,
                'row_total': row_total
            })

        #ค่าเสื่อม
        depreciation_list = request.form.getlist('depreciation_list')
        expenses = request.form.getlist('expenses', type=float)
        product_amount = request.form.getlist('product_amount', type=float)

        #บรรจุภัณฑ์
        package_list = request.form.getlist('package_list')
        package_price = request.form.getlist('package_price', type=float)
        package_amount = request.form.getlist('package_amount', type=float)

        #แรงงาน

        return render_template(
            'summary.html', 
            cost_total=grand_total,
            cost_data=all_cost_details
        )


if __name__ == "__main__":
    app.run(debug=True)

