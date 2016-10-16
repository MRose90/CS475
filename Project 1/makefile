proj1:
	g++ -DNUMT=1 proj0.cpp -o proj0 -lm -fopenmp
loop:
	echo "" > tst.csv; \
	for nums in 10 20 30 40 50 60 70 80 90 100 200 300 400 500 600 700 800 900 1000 2000 3000 4000 5000; do \
		for numt in 1 2 3 4 8 16 32 64 128; do \
			g++ -DNUMT=$$numt -DNUMS=$$nums p1.cpp -o p1 -lm -fopenmp ;\
			./p1 >>tst.csv ; \
		done; \
	done;
clean:
	rm -f *.o
