(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests)
  (map (lambda (lst) (cons first lst)) rests))

(define (zip pairs)
    (cons 
           (map (lambda (lst) (car lst)) pairs) 
           (cons (map (lambda (lst) (cadr lst)) pairs) nil)
     )
)
;; Problem 16
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 16
  (define (helper counter s)
    (if (null? s) s
      (cons (list counter (car s)) (helper (+ 1 counter) (cdr s)))))
  (helper 0 s)
)

  ; END PROBLEM 16

;; Problem 17
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  (cond
    ((= total 0) (cons nil nil))
    ((< total 0) nil)
    ((null? denoms) nil)
    (else
      (define using_current (list-change (- total (car denoms)) denoms))
      (define with_current (cons-all (car denoms) using_current))
      (define without_current (list-change total (cdr denoms)))
      (append with_current without_current)
    )
  )
)

;; Problem 18
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         expr
         )
        ((quoted? expr)
         expr
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           (cons form (cons params (map (lambda (elem) (let-to-lambda elem)) body)))
           ; END PROBLEM 18
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
            (cons `(lambda ,(car (zip values)) ,(let-to-lambda (car body))) (map (lambda (elem) (let-to-lambda elem)) (cadr (zip values))))
           ))
        (else
         ; BEGIN PROBLEM 18
            (map (lambda (elem) (let-to-lambda elem)) expr)
         ; END PROBLEM 18
         )))
