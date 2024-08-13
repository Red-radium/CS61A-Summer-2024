(define (cadr lst) (car (cdr lst)))

(define (make-kwlist1 keys values)
    (cons keys(cons values nil))    
)

(define (get-keys-kwlist1 kwlist)
    (define (helper keys)
        (if (null? keys)nil
            (cons (car keys) (helper (cdr keys)))
        )
    )
    (helper (car kwlist))
)

(define (get-values-kwlist1 kwlist)
    (define (helper keys)
        (if (null? keys)nil
            (cons (car keys) (helper (cdr keys)))
        )
    )
    (helper (cadr kwlist))
)




(define (make-kwlist2 keys values)
    (if (null? keys)
        nil
        (cons (list (car keys) (car values)) (make-kwlist2 (cdr keys) (cdr values)))
    )       
)

(define (get-keys-kwlist2 kwlist)
    (if (null? kwlist)nil
        (cons (car(car kwlist)) (get-keys-kwlist2 (cdr kwlist)))
    )
)

(define (get-values-kwlist2 kwlist)
    (if (null? kwlist)nil
        (cons (car(cdr(car kwlist))) (get-values-kwlist2 (cdr kwlist)))
    )
)

(define (add-to-kwlist kwlist key value)
    (make-kwlist (append (get-keys-kwlist kwlist) (list key)) (append (get-values-kwlist kwlist) (list value)))
)

(define (get-first-from-kwlist kwlist key)
    (define keys (get-keys-kwlist kwlist))
    (define values (get-values-kwlist kwlist))
    (if (null? keys) nil
        (if (equal? (car keys) key) (car values)
            (get-first-from-kwlist (make-kwlist (cdr keys) (cdr values)) key)
        )    
    )
)
