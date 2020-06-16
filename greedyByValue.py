# by value
import time

class ItemValue: 
      
    """Item Value DataClass"""
    def __init__(self, val, wt, ind):               
        self.val = val 
        self.wt = wt 
        
        self.ind = ind 
        self.cost = val
  
    def __lt__(self, other):        
        return self.cost < other.cost 
    
    
  
# Knapsack dengan Greedy Solution 
class GreedyByValue: 
      
    
    @staticmethod                                    
    def byValue(wt, val, capacity): 
          
        
        idx = [] 
        for i in range(len(val)): 
            idx.append(ItemValue(val[i], wt[i], i))
            
        # Sorting descending profit
        idx.sort(reverse = True)           
        c = 1
        print("*GREEDY BY PROFIT*")
        print("Sorting Berdasarkan Value / Profit secara descending")
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
                totVal += tempVal        #totVal = totVal + tempVal
                print("Sisa Kapasitas ketika dikurang weight dr objek - " + str(c) + " = "+ str(capacity))
                c = c+1
            
        print("karena sisa kapasitas pesawat = " + str(capacity) + " <" +" berat objek = "  +str(tempWt)+" maka Kapasitas tidak menampung")  
        print("Running Time = %s sec" % (time.time() - start_time))
        hasilSemua = ("Profit berdasarkan greedyByValue = " + str(totVal))
        return hasilSemua
        
  
# Main
if __name__ == "__main__":       
    # value (profit), berat Objek, dan kapasitas pesawat               
    brt = [100, 90, 75, 80]                             # objek dalam kg orang/barang
    val = [140, 250, 120, 200]                          # profit diambil ketika kelas/harga setiap objek berbeda
    kapasitas = 300                                     # Kapasitas Pesawat
    
    
    maxValue = GreedyByValue.byValue(brt, val, kapasitas) 
    print(maxValue) 
  