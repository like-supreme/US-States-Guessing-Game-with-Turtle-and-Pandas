""" turtle kullanarak abd eyaletlerini çizeceğiz
csv dosyasında eyalet isimleri ve koordinatları var
kısaca kullanıcı eyalet ismini yazdığında o eyaletin koordinatlarını alıp arkaplanda o koordintlara
isim yazılacak
eğlenceli bir oyun olacak gibi

onscreenclick() methodu ile tıklanan yerin koordinatlarını alabiliriz
csv dosyasında koşul ile isimlere bakıp ismin yanındaki koordinatları alıp ekrana onscreenclick ile 
yazdıracağız. 
mainloop() methodu ile ekran kapanmasın diye bekleyeceğiz
exitonclick alternatifi biraz. 

csvden okuma yapıp x ve y değerlerini alacağız

answer state den alınan girdinin lowerı for ile bütün csv içinde yazan eyaletler ile karşılaştırılacak
eğer eşleşirse o eyaletin x ve y koordinatları alınacak.

popup ekranda x/50 states correct yazıyor bunu da tasarla

1 convert the guess to title case
2 check if guess is among all the 50 states
3 write a correct guesses onto the map
4 use a loop to allow the user to keep guessing
5 record the correct guesses in a list 
6 keeep track of the score
"""