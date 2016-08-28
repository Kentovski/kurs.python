from django.shortcuts import render
from django.http import JsonResponse
import json

GOOGLE = '''
[
{"source_link": "http://www.google.com.ua/url?url=http://www.catster.com/topic/cat-dandy/&rct=j&q=&esrc=s&sa=U&ved=0ahUKEwiircX0gOXOAhXM1iwKHarWB4MQwW4IFzAB&usg=AFQjCNH8SVyYongL9i7kCi265bTZNlq3Pw", "direct_link": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSw9OK3LhTPa3CRdtf4khDJvxsIU1QqXHPoG9QFfhGVk4FEpAX-qCZ64gZ3"},
{"source_link": "http://www.google.com.ua/url?url=http://cats.petbreeds.com/&rct=j&q=&esrc=s&sa=U&ved=0ahUKEwiircX0gOXOAhXM1iwKHarWB4MQwW4IHTAE&usg=AFQjCNGGPeEcLb2EIuK48dLKIVm8wBD_AA", "direct_link": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTaKFV3BJIfybHOZx6jUWLr0mBCa2NxpEM65QhacczN4YVrOPk_jKN8oXQ"},
{"source_link": "http://www.google.com.ua/url?url=http://www.royalcanin.ca/products/cat-nutrition/adult-cat&rct=j&q=&esrc=s&sa=U&ved=0ahUKEwiircX0gOXOAhXM1iwKHarWB4MQwW4IHzAF&usg=AFQjCNGjfYabOHlmxsEOd0wyB16fKNB1Xw", "direct_link": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLjpD7FYx53hytWpWEgoiW-H8TRjMGAiOH-fsGhrLNgNpM-tX877tgyOnZ"},
{"source_link": "http://www.google.com.ua/url?url=http://trawelindia-mails.blogspot.com/2015/03/cute-cat-wallpapers.html&rct=j&q=&esrc=s&sa=U&ved=0ahUKEwiircX0gOXOAhXM1iwKHarWB4MQwW4IIzAH&usg=AFQjCNEpFk14QMRrlKJjZPSSCkSE7BQFRA", "direct_link": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRKWI0t_nK0U7u0Egb_8458fCdJjOM_hxrTHPzWpLzDX7Z0cEjexI-h6T8"},
{"source_link": "http://www.google.com.ua/url?url=http://www.bharatint.com/cats-grooming/c&rct=j&q=&esrc=s&sa=U&ved=0ahUKEwiircX0gOXOAhXM1iwKHarWB4MQwW4IITAG&usg=AFQjCNFXUSj3Lkype1g53UTWDHswQ3Pi2g", "direct_link": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTsLXr69FaMCSWPC0riCRxyeEEVNBrXOSfQ98WDKKIlH6raUCly7F7wHME"},
{"source_link": "http://www.google.com.ua/url?url=http://www.catprotection.com.au/adopt-a-cat-from-the-cat-protection-society/&rct=j&q=&esrc=s&sa=U&ved=0ahUKEwiircX0gOXOAhXM1iwKHarWB4MQwW4IKTAK&usg=AFQjCNG0FlSw06QEvckfHnfQRtvdawg-vg", "direct_link": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTxw3_3idCv8gD6BAfzm1Y9ihMaI2uGu3rgiG1ilGUp72gpRRiEgAMOXogq"},
{"source_link": "http://www.google.com.ua/url?url=http://www.petdrugsonline.co.uk/cats&rct=j&q=&esrc=s&sa=U&ved=0ahUKEwiircX0gOXOAhXM1iwKHarWB4MQwW4IJTAI&usg=AFQjCNHNTdwg-TfzezFNlAAVc4A7aavEgg", "direct_link": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcR-7fBp5ARUsFD3cIscpXY4umVtVliNhxYf6P59Diit1ocnHIdMW9hoaiA"},
{"source_link": "http://www.google.com.ua/url?url=https://pixabay.com/en/photos/cat/&rct=j&q=&esrc=s&sa=U&ved=0ahUKEwiircX0gOXOAhXM1iwKHarWB4MQwW4IGzAD&usg=AFQjCNFY9foro5dpMHRV6U75vM5apiBNKQ", "direct_link": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQZ_BPRDfjivEwrCXCbxUIyP6ZM97PdxRauXMP1nOqV4ypNCIyc0boGcXE"},
{"source_link": "http://www.google.com.ua/url?url=https://www.royalcanin.com/products/cat/adult&rct=j&q=&esrc=s&sa=U&ved=0ahUKEwiircX0gOXOAhXM1iwKHarWB4MQwW4IGTAC&usg=AFQjCNHffa4aX0dhivKH4hQJAlrUwTfTPQ", "direct_link": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRJyNVc64ILUEDKNducIjY-eKeDF4eqATvV3FlrsRp5Sf43JidOBxgvvzk"},
{"source_link": "http://www.google.com.ua/url?url=https://www.royalcanin.com/products/cat/breed-nutrition&rct=j&q=&esrc=s&sa=U&ved=0ahUKEwiircX0gOXOAhXM1iwKHarWB4MQwW4IKzAL&usg=AFQjCNEj7ebkFPMiSljbc_Gib6sLHQPlOA", "direct_link": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRbp9g3Nq5buObnoA8-YIp7XRGE_CIPR0nns1RsMo8iSLRSriPWOF3XwMM"},
{"source_link": "http://www.google.com.ua/url?url=http://www.boredpanda.com/surprised-cat-hydrocephalus-kevin-theadventuresofkev/&rct=j&q=&esrc=s&sa=U&ved=0ahUKEwiircX0gOXOAhXM1iwKHarWB4MQwW4IMTAO&usg=AFQjCNEWzWZf_Iw22lowY7fNLLymAp6-pg", "direct_link": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRaRsdP876o1oLTs70NfADWPTMrminxFoHldN-8Os5aAj7Q_r37TU9QudQ"},
{"source_link": "http://www.google.com.ua/url?url=https://www.battersea.org.uk/cats/cat-rehoming-gallery&rct=j&q=&esrc=s&sa=U&ved=0ahUKEwiircX0gOXOAhXM1iwKHarWB4MQwW4IFTAA&usg=AFQjCNFEqq6JjHnVQnxcHI0gVzI4Q9L3ZQ", "direct_link": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRA875Catuzxws9dXOxNv_C11eC7Lr1qxePn4r-4BGytTt2EqSHthHMdw"},
{"source_link": "http://www.google.com.ua/url?url=https://www.royalcanin.com/products/cat&rct=j&q=&esrc=s&sa=U&ved=0ahUKEwiircX0gOXOAhXM1iwKHarWB4MQwW4ILTAM&usg=AFQjCNHjlYeHDGR1BfSmGiVu9YN8dAQLIA", "direct_link": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSX7-3IZ08U7H4j9GkFt13GuDS-Egf7dGMtU9eA7I5Fztki5h6AMreUewo"},
{"source_link": "http://www.google.com.ua/url?url=https://www.youtube.com/watch%3Fv%3DtntOCGkgt98&rct=j&q=&esrc=s&sa=U&ved=0ahUKEwiircX0gOXOAhXM1iwKHarWB4MQwW4IJzAJ&usg=AFQjCNHFkMvjOfq7g_cg-Di1TRTTGRYz-g", "direct_link": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMnDp0nNBLHwunbh2DDIBhN_Cj9zwRPq-Hp0sB-LlSWy2ijcFs-uyD-vE"},
{"source_link": "http://www.google.com.ua/url?url=http://www.rd.com/advice/pets/how-to-decode-your-cats-behavior/&rct=j&q=&esrc=s&sa=U&ved=0ahUKEwiircX0gOXOAhXM1iwKHarWB4MQwW4INTAQ&usg=AFQjCNFvNfgmaNlH2YO8kzB6owUr3SOe6Q", "direct_link": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQjPlK7k97vKZWvnvSXAKFErMI4mWXsHZ1goZbs-BSLAVDXtvLY3o_REn0"}
]
'''
YANDEX = '''
[{"direct_link": "http://bolen-kot.net.ru/wp-content/uploads/2015/09/123.jpg", "source_link": "http://bolen-kot.net.ru/cat-health/about-diseases/zapor-u-koshek/"},
{"direct_link": "http://sf.co.ua/14/05/wallpaper-782249.jpg", "source_link": "http://sf.co.ua/id137677"},
{"direct_link": "http://cos.h-cdn.co/assets/14/29/1600x800/nrm_1405536406-484734347.jpg", "source_link": "http://www.cosmopolitan.com/entertainment/movies/news/a32763/the-grumpy-cat-movie-trailer/"},
{"direct_link": "http://vashipitomcy.ru/_pu/0/10395728.jpg", "source_link": "http://vashipitomcy.ru/publ/zdorove/kastracija_i_sterilizacija/kastracija_kotov_podgotovka_k_procedure_i_posleoperacionnyj_ukhod/17-1-0-58?_escaped_fragment_="},
{"direct_link": "http://e2ua.com/data/wallpapers/230/WDF_2668026.png", "source_link": "http://e2ua.com/group/cat/"},
{"direct_link": "http://images.forwallpaper.com/files/images/0/0f36/0f368fc0/785849/cat-wallpaper-background-widescreen-animal.jpg", "source_link": "http://ru.forwallpaper.com/wallpaper/cat-wallpaper-background-widescreen-animal-785849.html"},
{"direct_link": "https://i.ytimg.com/vi/fGavmE6Emuo/maxresdefault.jpg", "source_link": "http://mir-shoping.ru/watch/fGavmE6Emuo"},
{"direct_link": "http://animal-store.ru/img/2015/043011/5330409", "source_link": "http://animal-store.ru/pet/%D0%B4%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%8F%D1%8F-%D0%BA%D0%BE%D1%88%D0%BA%D0%B0/"},
{"direct_link": "http://animal-store.ru/img/2015/050101/4000343", "source_link": "http://animal-store.ru/pet/%D0%BA%D0%BE%D1%88%D0%BA%D0%B8-%D0%B2%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F/"},
{"direct_link": "http://www.chaniapost.eu/wp-content/uploads/2015/11/cat.jpg", "source_link": "http://www.chaniapost.eu/2015/11/01/goodbye-one-eye-you-were-a-good-cat/"},
{"direct_link": "http://www.cobra.ua/pictures/101434/66216563.jpg", "source_link": "http://www.cobra.ua/item/101434/smartfon_cat_caterpillar_s30_dual_sim_black"},
{"direct_link": "http://www.fullhdoboi.ru/_ph/29/16131122.jpg", "source_link": "http://www.fullhdoboi.ru/photo/29-0-28894-3?1464812297"},
{"direct_link": "http://www.nastol.com.ua/pic/201205/1920x1080/nastol.com.ua-23777.jpg", "source_link": "http://www.nastol.com.ua/download/23777/1920x1080/"},
{"direct_link": "http://sf.co.ua/14/01/wallpaper-505162.jpg", "source_link": "http://sf.co.ua/id111295"},
{"direct_link": "http://i.wp-b.com/media/2016-6-28/_omgl-Kqam.jpg", "source_link": "http://wp-b.com/795579"},
{"direct_link": "http://www.coollady.ru/pic/0003/074/01.jpg", "source_link": "http://www.coollady.ru/index.php/html/index.php?name=Pages&op=page&pid=4085"},
{"direct_link": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Cat_March_2010-1.jpg", "source_link": "http://imgstocks.com/file-cat-march-2010-1-jpg-wikimedia-commons.html"}]
'''
INSTAGRAM = '''
[{"source_link": "https://www.instagram.com/p/BJoM7LUAD0d", "direct_link": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/14026736_290630224632074_288854779_n.jpg?ig_cache_key=MTMyNjM2NjkzMzQxNDU5MTc3Mw%3D%3D.2"},
{"source_link": "https://www.instagram.com/p/BJoM68IAQOW", "direct_link": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/14099651_1677997355858168_2146854786_n.jpg?ig_cache_key=MTMyNjM2NjkxNzEwNzE4ODYzMA%3D%3D.2"},
{"source_link": "https://www.instagram.com/p/BJoM66Hh-tC", "direct_link": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/14026801_923371211108334_1551802115_n.jpg?ig_cache_key=MTMyNjM2NjkxNDk1MTc2ODg5OA%3D%3D.2"},
{"source_link": "https://www.instagram.com/p/BJoM6yVAlJl", "direct_link": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/13768343_1765001177121726_537765646_n.jpg?ig_cache_key=MTMyNjM2NjkwNjU4Nzk1OTkwOQ%3D%3D.2"},
{"source_link": "https://www.instagram.com/p/BJoM6lFghUu", "direct_link": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/14032808_691792824301259_316009809_n.jpg?ig_cache_key=MTMyNjM2Njg5MjM2OTI1MzY3OA%3D%3D.2"},
{"source_link": "https://www.instagram.com/p/BJoM6ieDpE0", "direct_link": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/13687383_534418856758461_1516854459_n.jpg?ig_cache_key=MTMyNjM2Njg4OTU1OTg4ODE4MA%3D%3D.2"},
{"source_link": "https://www.instagram.com/p/BJoM6g0gTaD", "direct_link": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/13741312_1097729603641616_2100139764_n.jpg?ig_cache_key=MTMyNjM2Njg4Nzc4OTAxNjcwNw%3D%3D.2"},
{"source_link": "https://www.instagram.com/p/BJoM6aCh8a9", "direct_link": "https://scontent-waw1-1.cdninstagram.com/t51.2885-15/e35/13687227_1175130019216465_1259588341_n.jpg?ig_cache_key=MTMyNjM2Njg4MDUwODEzNTEwMQ%3D%3D.2"}]
'''

def index(request):
    if request.GET:
        print(request.GET['query'])
        return JsonResponse({
                'google': json.loads(GOOGLE),
                'yandex': json.loads(YANDEX),
                'instagram': json.loads(INSTAGRAM),
            })
    return render(request, 'index.html')
