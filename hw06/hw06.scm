;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (sign x)
  (cond
    ((= x 0) 0)
    ((< x 0) -1)
    (else 1)
      )
)

(define (square x) (* x x))

(define (pow b n)
  (cond
    ((= n 0) 1)
    ((even? n) (pow (square b) (/ n 2)))
    ((odd? n) (* b (pow (square b) (/ (- n 1) 2))))
      )
)

(define (unique s)
   (cond
        ((null? s) 
            s)
    (else (cons (car s) (unique (filter (lambda (x) (not (eq? x (car s)))) (cdr s)))))))


