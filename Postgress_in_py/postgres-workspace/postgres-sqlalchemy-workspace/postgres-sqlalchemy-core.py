
from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData

engine = create_engine('postgres://postgres:smith3dx@localhost/red30')

with engine.connect() as connection:
    meta = MetaData(engine)
    sales_table = Table('sales', meta, autoload=True, autoload_with=engine)

    insert_statement = sales_table.insert().values(order_num=1105913,
                                                order_type='Retail',
                                                cust_name='Smith ryan',
                                                prod_number='EB544',
                                                prod_name= 'understanding Nigeria',
                                                quantity=5,
                                                price=19.5,
                                                discount=0,
                                                order_total=58.5)

    connection.execute(insert_statement)

    #read
    select_statement = sales_table.select().limit(10)
    result_set = connection.execute(select_statement)
    for r in result_set:
        print(r)

    #update
    update_statement = sales_table.update().where(sales_table.c.order_num==1105913).values(quantity=2, order_total=39)
    connection.execute(update_statement)

    #confirm update: read 
    reselect_statement = sales_table.select().where(sales_table.c.order_num==1105913)
    update_set = connection.execute(reselect_statement)
    for u in update_set:
        print(u)

    #Delete
    delete_statment = sales_table.delete().where(sales_table.c.order_num==1105913)
    connection.execute(delete_statment)

    #confirm Delete: read
    not_found_set = connection.execute(reselect_statement)
    print(not_found_set.rowcount)
