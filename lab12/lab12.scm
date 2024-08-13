(define (no-repeats s)
    (cond
        ((null? s) nil)
        (else (cons (car s) 
        (no-repeats 
        (filter (lambda (x) (not (= x (car s)))))(cdr lst))))
    )
)

(define (without-duplicates lst)

)

(define (reverse lst)
    (if (null? lst) nil
        (append (reverse (cdr lst)) (list (car lst)))
    )
)
