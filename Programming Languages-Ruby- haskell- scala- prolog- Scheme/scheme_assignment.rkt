#lang racket
(define make-seq-list
  (lambda (x y)
    (cond
      (( = x y) (list x))
      (else (cons x (make-seq-list (+ x 1) y))))))
(define make-whole-list
  (lambda (x)
    (make-seq-list 1 x)))

(define find-ith-element
  (lambda (list1 elem)
    (cond
      ((> elem (listLength list1)) #F)
      ((= 0 elem) (car list1))
      (else (find-ith-element (cdr list1) (- elem 1))))))

(define lastElement
  (lambda (list1)
    (cond
      ((null? list1) "List empty")
      ((= (listLength list1) 1) (car list1))
      (else (lastElement (cdr list1))))))

(define listLength
  (lambda (list1)
    (cond
      ((null? list1 ) 0)
       (else
       (+ 1 (listLength(cdr list1)))))))

(define concatList
  (lambda (list1 list2)
    (cond
      ((null? list2) list1)
      ((null? list1) "Both lists empty")
      (else (concatList(cons list1 (car list2)) (cdr list2))))))

(define reverseList
  (lambda (lis)
    (cond
      ((null? lis) '())
      ( else (cons (lastElement lis) (reverseList (removeLast lis)))))))

(define (removeLast list1)
  (if(null? (cdr list1)) '()
  (cons(car list1)(removeLast(cdr list1)))))


(define (minElement list1)
  (cond
    ((null? list1)       
     #f)
    ((null? (cdr list1))
     (car list1))
    ((> (car list1) (cadr list1))
     (minElement (cdr list1)))
    (else 
     (minElement (cons (car list1) (cddr list1))))))

(define (maxElement list1)
  (cond
    ((null? list1)       
     #f)
    ((null? (cdr list1))
     (car list1))
    ((< (car list1) (cadr list1))
     (maxElement (cdr list1)))
    (else 
     (maxElement (cons (car list1) (cddr list1))))))

(define odd
  (lambda (list1)
    (if (or (null? list1)
            (null? (cdr list1)))
        '()
        (cons (car list1)
              (odd (cddr list1)))
        )
    )
  )

(define even
  (lambda (list1)
    (if (or (null? list1)
            (null? (cdr list1)))
        '()
        (cons (cadr list1)
              (even (cddr list1)))
        )
    )
  )

(define (merge list1 list2)
  (cond
    ((null? list1) list2)
    ((null? list2) list1)
    ((< (car list1) (car list2))
     (cons (car list1) (merge(cdr list1) list2))
     )
    (#t 
     (cons (car list2) (merge list1 (cdr list2)))
     )
    )
  )

(define (mergeSort y)
  (cond
    ((or (null? y) (null? (cdr y))) y)
    ((null? (cddr y))
     (merge(list (car y)) (cdr y)))
    (#t
     (let ((x (ceiling (/ (length y) 2))))
       (merge(mergeSort (take y x))
             (mergeSort (drop y x)))))
    )
  )




