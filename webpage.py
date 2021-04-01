from flask import Blueprint, request, redirect, url_for, render_template
import function

webpage = Blueprint('webpage', url_prefix='/lunch', __name__)  # static_folder=None, static_url_path=None, template_folder=None, url_prefix=None, subdomain=None

@webpage.route('/')
def page_index():
    return 'This is myschool-mylunch-webpage'


#====================================
@webpage.route('/order' methods=['GET', 'POST'])
def page_order():
    if request.method == 'POST':
        #取得session_id、預定之日期、訂單種類id及數量、總金額(用於核對)
        #確認是本人才可進行交易
        return 'This is order_process'
    else:
        #取得菜單資料
        return 'This is order'
        #return render_template('order.html', ... )


@webpage.route('/menu')
def page_menu():
    #取得今日日期(date)(YYYYMMDD)
    return redirect(f'menu/{date}')
    #return render_template('menu.html')
    
    
@webpage.route('/menu/<date>')
def page_menu_date(date):
    #取得菜單資料
    return 'This is menu(date)'
    #return render_template('menu.html', ... )

    
@webpage.route('/menu/manage', methods=['GET', 'POST'])
def page_menu_manage():
    #if request.method == 'POST':
    #  取得session_id、新增/更改內容
    #  if身分符合:
    #    照著內容更改
    #    return render_template()
    #else:
    #  取得session_id
    #  if身分符合:
    #    return render_template()
    #return 'ACCESS_DENIED'
    return 'This is menu_manage'


@webpage.route('/orders/list')
def page_orders_list():
    #?filter
    #取得訂單資料(有filter就照做)
    #return render_template()
    return 'This is orders_list'

@webpage.route('/orders/edit/<orders_id>')
def page_orders_edit(orders_id):
    #取得session_id、 ... 
    #確認身分
    return 'This is orders_edit'

@webpage.route('/orders/delete/<orders_id>')
def page_orders_delete(orders_id):
    #取得session_id、 ... 
    #確認身分
    return 'This is orders_delete'
