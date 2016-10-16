proj0:
	g++ -DNUMT=1 proj0.cpp -o proj0 -lm -fopenmp
loop:
	for t in 1,4,8; do \
		g++ -DNUMT=$t proj0.cpp -o proj0 -lm -fopenmp ;\
		./proj0 ; \
	done;
non-loop:
	g++ -DNUMT=1 proj0.cpp -o proj0-1 -lm -fopenmp
	g++ -DNUMT=4 proj0.cpp -o proj0-4 -lm -fopenmp
	g++ -DNUMT=8 proj0.cpp -o proj0-8 -lm -fopenmp
	./proj0-1
	./proj0-4
	./proj0-8
clean:
	rm -f *.o
