# by weight
import time

class ItemValue: 
      
    """Item Value DataClass"""
    def __init__(self, wt, val, ind):               
        self.wt = wt 
        self.val = val 
        # self.hrg = hrg
        self.ind = ind 
        self.cost = wt 
  
    def __lt__(self, other):        
        return self.cost < other.cost 
  
# Knapsack dengan Greedy Solution 
class GreedyByWeight: 
      
    
    @staticmethod                                    
    def byWeight(wt, val, capacity): 
          
        
        idx = [] 
        for i in range(len(wt)): 
            idx.append(ItemValue(wt[i], val[i], i))
            
        # Sorting asscending weight
        idx.sort(reverse = False)           
        c = 1
        print("*GREEDY BY WEIGHT*")
        print("Sorting Berdasarkan Weight secara ascending")
        print("=======================================================================")
        for i in idx: 
            print("Objek ke - " + str(c)) 
            print("weight dengan alamat = " + str(i.wt))
            print("profit dengan alamat = " + str(i.val)) 
            print("=======================================================================")
            c = c+1
        totVal = 0
        print("Kapasitas Awal Pesawat = " + str(capacity))
        
        c = 1
        start_time = time.time()
        for i in idx: 
            tempWt = int(i.wt) 
            tempVal = int(i.val) 
            
            if capacity - tempWt >= 0: 
                capacity -= tempWt           #capacity = capaciity - tempWt
                totVal += tempVal            #totVal = totVal + tempVal
                print("Sisa Kapasitas ketika dikurang weight dr objek - " + str(c) + " = "+ str(capacity))
                c = c+1
            
        print("karena sisa kapasitas pesawat = " + str(capacity) + " <" +" berat objek = "  +str(tempWt)+" maka Kapasitas tidak menampung")
        print("Running Time = %s sec" % (time.time() - start_time))    
        hasilSemua = ("Profit berdasarkan greedyByWeight= " + str(totVal))    
        return hasilSemua
        
  
# Main
if __name__ == "__main__":    
    # value (profit), berat Objek, dan kapasitas pesawat                   
    brt = [100, 90, 75, 80]                             # objek dalam kg orang/barang
    val = [140, 250, 120, 200]                          # profit diambil ketika kelas/harga setiap objek berbeda
    kapasitas = 300                                     # Kapasitas Pesawat
    
  
    maxValue = GreedyByWeight.byWeight(brt, val, kapasitas) 
    print(maxValue) 
  