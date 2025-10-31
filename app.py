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
        depreciation_total = 0.0
        for expense, amount in zip(expenses, product_amount):
            
            row_total = 0.0
            
            # ป้องกันการหารด้วย 0 (ZeroDivisionError)
            if amount > 0:
                # สูตรคำนวณต้นทุนของแถวนี้
                # (ราคา / ปริมาณทั้งหมด) * จำนวนที่ใช้
                row_total = expense/amount
            
            # เพิ่มต้นทุนแถวนี้ เข้าไปในยอดรวมทั้งหมด
            depreciation_total += row_total

        #บรรจุภัณฑ์
        package_price = request.form.getlist('package_price', type=float)
        package_amount = request.form.getlist('package_amount', type=float)
        package_total = 0.0
        for package_price, amount in zip(package_price, package_amount):
            
            row_total = 0.0
            
            # ป้องกันการหารด้วย 0 (ZeroDivisionError)
            if amount > 0:
                # สูตรคำนวณต้นทุนของแถวนี้
                # (ราคา / ปริมาณทั้งหมด) * จำนวนที่ใช้
                row_total = package_price/amount
            
            # เพิ่มต้นทุนแถวนี้ เข้าไปในยอดรวมทั้งหมด
            package_total += row_total

        #แรงงาน
        all_labor = request.form.get('all_labor', type=float)
        amount_labor = request.form.get('amount_labor', type=float)
        labor_total = 0.0
        if amount_labor > 0:
            #สูตรคำนวณต้นทุนเงินเดือน
            labor_total = all_labor/amount_labor

        #ผลรวมต้นทุนสินค้าทั้งหมด
        product_cost = cost_total + depreciation_total + package_total + labor_total

        return render_template(
            'summary.html', 
            cost_total=cost_total,
            depreciation_total=depreciation_total,
            package_total=package_total,
            labor_total=labor_total,
            product_cost = product_cost
        )

if __name__ == "__main__":
    app.run(debug=True)
