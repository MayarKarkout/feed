import feedparser

# rawdata = """<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0">
#                   <channel><item>
#                   <g:id>100130</g:id>
#                   <link><![CDATA[https://www.rajapack.pl/higiena-catering/przemyslowe-srodki-czystosci/czysciwa-przemyslowe/recznik-papierowy-mala-rolka-11-szt_sku100130.html?priceVAT=true&ForceCustomerType=true]]></link>
#                   <g:price>230.01 PLN</g:price>
#                   <g:availability>in stock</g:availability>
#                   <g:google_product_category>Dom i ogród > Akcesoria łazienkowe</g:google_product_category>
#                   <title>Ręcznik papierowy mała rolka 11 szt</title>
#                   <g:image_link><![CDATA[https://raja.scene7.com/is/image/Raja/products/recznik-papierowy-mala-rolka-11-szt_100130.jpg?image=M_100130_D_S_055_F$default$]]></g:image_link>
#                   <g:description><![CDATA[Ręcznik papierowy mała rolka 11 szt]]></g:description>
#                   <g:brand>Rajapack</g:brand>
#                   <g:mpn>100130</g:mpn>
#                   <g:condition>nowy</g:condition>
#                   <g:multipack></g:multipack>
#                   <g:custom_label_0></g:custom_label_0>
#                   <g:custom_label_1></g:custom_label_1>
#                   <g:custom_label_2></g:custom_label_2>
#                   <g:custom_label_3>Higiena i bezpieczeństwo</g:custom_label_3>
#                   </item><item>
#                   <g:id>100134</g:id>
#                   <link><![CDATA[https://www.rajapack.pl/higiena-catering/przemyslowe-srodki-czystosci/czysciwa-przemyslowe/recznik-papierowy-duza-rolka-6-szt_sku100134.html?priceVAT=true&ForceCustomerType=true]]></link>
#                   <g:price>265.68 PLN</g:price>
#                   <g:availability>idsn stock</g:availability>
#                   <g:google_product_category>Dom i ogród > Akcesoria łazienkowe</g:google_product_category>
#                   <title>Ręcznik papierowy duża rolka 6 szt</title>
#                   <g:image_link><![CDATA[https://raja.scene7.com/is/image/Raja/products/recznik-papierowy-duza-rolka-6-szt_100134.jpg?image=M_100130_D_S_055_F$default$]]></g:image_link>
#                   <g:description><![CDATA[Ręcznik papierowy duża rolka 6 szt]]></g:description>
#                   <g:brand>Rajapack</g:brand>
#                   <g:mpn>100134</g:mpn>
#                   <g:condition>nowy</g:condition>
#                   <g:multipack></g:multipack>
#                   <g:custom_label_0></g:custom_label_0>
#                   <g:custom_label_1></g:custom_label_1>
#                   <g:custom_label_2></g:custom_label_2>
#                   <g:custom_label_3>Higiena i bezpieczeństwo</g:custom_label_3>
#                   </item>"""

feed = feedparser.parse('/simple.txt')


# d = feedparser.parse(rawdata)
d = feed
print(len(d.entries))

available_items = 0
for entry in d.entries:
    if entry.g_availability == "in stock":
        available_items = available_items + 1

print("Available items:")
print(available_items)


# print(d['entries'])
