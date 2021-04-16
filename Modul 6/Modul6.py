#1
from MhsTIF import MhsTIF
c0 = MhsTIF('Ika',10,'Sukoharjo',240000)
c1 = MhsTIF('Budi',51,'Sragen',230000)
c2 = MhsTIF('Ahmad',2,'Surakarta',250000)
c3 = MhsTIF('Chandra',18,'Surakarta',235000)
c4 = MhsTIF('Eka',4,'Boyolali',230000)
c5 = MhsTIF('Fandi',31,'Salatiga',250000)
c6 = MhsTIF('Deni',13,'Klaten',245000)
c7 = MhsTIF('Galuh',5,'Wonogiri',245000)
c8 = MhsTIF('Janto',23,'Klaten',245000)
c9 = MhsTIF('Hasan',64,'Karanganyar',270000)
c10 = MhsTIF('Khalid',29,'Purwodadi',265000)
daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def mergeSort(data):
    if len(data) > 1:
        mid = len(data) // 2
        separuhKiri = data[:mid]
        separuhKanan = data[mid:]

        mergeSort(separuhKiri)
        mergeSort(separuhKanan)
        i=0; j=0; k=0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i].NIM < separuhKanan[j].NIM:
                data[k] = separuhKiri[i]
                i = i + 1
            else:
                data[k] = separuhKanan[j]
                j = j +1
            k = k + 1
        while i < len(separuhKiri):
            data[k] = separuhKiri[i]
            i = i + 1
            k = k + 1
        while j < len(separuhKanan):
            data[k] = separuhKanan[j]
            j = j + 1
            k = k + 1
##print("MergeSort")
##for i in daftar:
##    print(i.NIM)
##mergeSort(daftar)
##print("Sesudah")
##for i in daftar:
##    print(i.NIM)

def quickSort(data):
    quickSortBantu(data, 0, len(data)-1)
    
def quickSortBantu(data, awal, akhir):
    if awal<akhir:
        titikBelah = partisi(data, awal, akhir)
        quickSortBantu(data, awal, titikBelah-1)
        quickSortBantu(data, titikBelah+1, akhir)
        
def partisi(data, awal, akhir):
    nilaiPivot = data[awal].NIM
    penandaKiri = awal + 1
    penandaKanan = akhir
    selesai = False
    
    while not selesai:
        while penandaKiri <= penandaKanan and data[penandaKiri].NIM <= nilaiPivot:
            penandaKiri = penandaKiri + 1           
        while penandaKanan >= penandaKiri and data[penandaKanan].NIM >= nilaiPivot:
            penandaKanan = penandaKanan - 1
        if penandaKanan < penandaKiri:
            selesai = True
        else:
            temp = data[penandaKiri]
            data[penandaKiri] = data[penandaKanan]
            data[penandaKanan] = temp
    temp = data[awal]
    data[awal] = data[penandaKanan]
    data[penandaKanan] = temp
    
    return penandaKanan

##print("QuickSort")
##for i in daftar:
##    print(i.NIM)
##quickSort(daftar)
##print("Sesudah")
##for i in daftar:
##    print(i.NIM)

#3
##def mergeSort(data):
##    if len(data) > 1:
##        mid = len(data) // 2
##        separuhKiri = data[:mid]
##        separuhKanan = data[mid:]
##
##        mergeSort(separuhKiri)
##        mergeSort(separuhKanan)
##
##        i=0; j=0; k=0
##        while i < len(separuhKiri) and j < len(separuhKanan):
##            if separuhKiri[i] < separuhKanan[j]:
##                data[k] = separuhKiri[i]
##                i = i + 1
##            else:
##                data[k] = separuhKanan[j]
##                j = j +1
##            k = k + 1
##
##        while i < len(separuhKiri):
##            data[k] = separuhKiri[i]
##            i = i + 1
##            k = k + 1
##
##        while j < len(separuhKanan):
##            data[k] = separuhKanan[j]
##            j = j + 1
##            k = k + 1
##
##def quickSort(data):
##    quickSortBantu(data, 0, len(data)-1)
##def quickSortBantu(data, awal, akhir):
##    if awal<akhir:
##        titikBelah = partisi(data, awal, akhir)
##        quickSortBantu(data, awal, titikBelah-1)
##        quickSortBantu(data, titikBelah+1, akhir)
##def partisi(data, awal, akhir):
##    nilaiPivot = data[awal]
##    penandaKiri = awal + 1
##    penandaKanan = akhir
##    selesai = False
##    while not selesai:
##        while penandaKiri <= penandaKanan and data[penandaKiri] <= nilaiPivot:
##            penandaKiri = penandaKiri + 1
##            
##        while penandaKanan >= penandaKiri and data[penandaKanan] >= nilaiPivot:
##            penandaKanan = penandaKanan - 1
##
##        if penandaKanan < penandaKiri:
##            selesai = True
##        else:
##            temp = data[penandaKiri]
##            data[penandaKiri] = data[penandaKanan]
##            data[penandaKanan] = temp
##    temp = data[awal]
##    data[awal] = data[penandaKanan]
##    data[penandaKanan] = temp
##
##    return penandaKanan
##
##
##from ASDModul5 import bubbleSort, selectionSort, insertionSort
##from time import time as detak
##from random import shuffle as kocok
##import time
##k = [[i] for i in range(1, 6001)]
##kocok(k)
##u_bub = k[:]
##u_sel = k[:]
##u_ins = k[:]
##u_mrg = k[:]
##u_qck = k[:]
##
##aw=detak();bubbleSort(u_bub);ak=detak();print('Bubble: %g detik' %(ak-aw) );
##aw=detak();selectionSort(u_sel);ak=detak();print('Selection: %g detik' %(ak-aw) );
##aw=detak();insertionSort(u_ins);ak=detak();print('Insertion: %g detik' %(ak-aw) );
##aw=detak();mergeSort(u_mrg);ak=detak();print('Merge: %g detik' %(ak-aw) );
##aw=detak();quickSort(u_qck);ak=detak();print('Quick: %g detik' %(ak-aw) );

#5
daftar = [54,26,93,17,77,31,44,55,20]
def mergeSort2(A, awal, akhir):
    mid = (awal+akhir)//2
    if awal < akhir:
        mergeSort2(A, awal, mid)
        mergeSort2(A, mid+1, akhir)
    a, f, l = 0, awal, mid+1
    tmp = [None] * (akhir - awal + 1)
    while f <= mid and l <= akhir:
        if A[f] < A[l]:
            tmp[a] = A[f]
            f += 1
        else:
            tmp[a] = A[l]
            l += 1
        a += 1
#proses penggabungan
    if f <= mid:
        tmp[a:] = A[f:mid+1]
    if l <= akhir:
        tmp[a:] = A[l:akhir+1]
#memindah isi tmp ke A
    a = 0
    while awal <= akhir:
        A[awal] = tmp[a]
        awal += 1
        a += 1
        
def mergeSort(A):
    mergeSort2(A, 0, len(A)-1)

##print("sebelum","\n",daftar)
##mergeSort(daftar)
##print("sesudah","\n",daftar)

#6
daftar = [54,26,93,17,77,31,44,55,20]
def quickSort(L, ascending = True): 
    quickSorthelp(L, 0, len(L), ascending)
    
def quickSorthelp(L, low, high, ascending = True): 
    result = 0
    if low < high: 
        pivot_location, result = Partition(L, low, high, ascending)  
        result += quickSorthelp(L, low, pivot_location, ascending)  
        result += quickSorthelp(L, pivot_location + 1, high, ascending)
    return result


def Partition(L, low, high, ascending = True):
    result = 0 
    pivot, pidx = median_of_three(L, low, high)
    L[low], L[pidx] = L[pidx], L[low]
    i = low + 1
    for j in range(low + 1, high, 1):
        result += 1
        if (ascending and L[j] < pivot) or (not ascending and L[j] > pivot):
            L[i], L[j] = L[j], L[i]  
            i += 1
    L[low], L[i - 1] = L[i - 1], L[low] 
    return i - 1, result

def median_of_three(L, low, high):
    mid = (low + high - 1) // 2
    a = L[low]
    b = L[mid]
    c = L[high - 1]
    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, high - 1
    if b <= c <= a:
        return c, high - 1
    return a, low

##print("sebelum","\n",daftar)
##quickSort(daftar)
##print("sesudah","\n",daftar)

#7
from time import time as detak
from random import shuffle as kocok
import time

def mergeSort_5(A):
    mergeSort2(A, 0, len(A)-1)


#quick sort terbaru
def quickSort_6(L, ascending = True): 
    quickSorthelp(L, 0, len(L), ascending)

k =  [[i] for i in range(1, 6001)]
kocok(k)
u_mer = k[:]
u_mer5 = k[:]
u_qui = k[:]
u_qui6 = k[:]

##aw=detak();mergeSort(u_mer);ak=detak();print("mergesort           : %g detik" %(ak-aw));
##aw=detak();mergeSort_5(u_mer5);ak=detak();print("mergesort terbaru  : %g detik" %(ak-aw));
##aw=detak();quickSort(u_qui);ak=detak();print("quicksort           : %g detik" %(ak-aw));
##aw=detak();quickSort_6(u_qui6);ak=detak();print("quicksort terbaru  : %g detik" %(ak-aw));

#8
class Node():
    def __init__(self,data,next= None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Linked():
    def __init__(self,head = None):
        self.head = head

    def cetak(self):
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next
    def appendList(self, data):
        node = Node(data)
        if self.head == None:
          self.head = node
        else:
          curr = self.head
          while curr.next != None:
            curr = curr.next
        curr.next = node

    def appendSorted(self, data):
        node = Node(data)
        curr = self.head
        prev = None

        while curr is not None and curr.data < data:
          prev = curr
          curr = curr.next
                    
        if prev == None:
          self.head = node
        else:
          prev.next = node

        node.next = curr

    def printList(self):
        curr = self.head
        while curr != None:
          print ("%d"%curr.data),
          curr = curr.next
          
    def mergeSorted(self, list1, list2):
        if list1 is None:
          return list2
        if list2 is None:
          return list1
        if list1.data < list2.data:
          temp = list1
          temp.next = self.mergeSorted(list1.next, list2)
        else:
          temp = list2
          temp.next = self.mergeSorted(list1, list2.next)
        return temp
    
##list1 = Linked()
##list1.appendSorted(48)
##list1.appendSorted(92)
##list1.appendSorted(33)
##list1.appendSorted(16)
##list1.appendSorted(17)
##print("List 1 :"),
##list1.printList()
##list2 = Linked()
##list2.appendSorted(23)
##list2.appendSorted(10)
##list2.appendSorted(18)
##print("List 2 :"),
##list2.printList()
##list3 = Linked()
##list3.head = list3.mergeSorted(list1.head, list2.head)
##print("Mergesort Linked list :"),
##list3.printList()
