<?php

use OrderServiceFactory;
use Services\FSM;
use Services\FSMInterface;

Class OrderService implements OrderServiceInterface {

    /**
     * Type OrderServiceFactory $factory
     */
    private $factory;

    /**
     * @return OrderService
     */
    public function __construct() {
        $this->build();
    }

    /**
     * @return void
     */
    private function build() {
        $this->factory = new OrderServiceFactory();
    }

    /**
     * @return FSMInterface
     */
    private function createState(int $orderId): FSMInterface {
        return $this->factory->createFSM($orderId);
    }

    /**
     * @return int
     */
    private function generateOrderId(): int {
        return rand();
    }

    /**
     * @inherit
     */
    public function changeState(int $orderId, string $status, string $event): bool {
        try {
            $fsa = $this->createState($orderId);
            $fsa->changeState($orderId, $status, $event);
        } catch (\Exception $e) {
            # Log Exception $e->getMessage()
            return False;    
        }

        return True;
    }

    /**
     * @return FSMInterface
     */
    public function create(): FSMInterface {
       
        $orderId = $this->generateOrderId();

        return $this->createState($orderId);
    }

    /**
     * @param int $orderId
     * 
     * @return string
     */
    public function getState($orderId): string {
        $fsa = $this->createState($orderId);

        return $fsa->getState();
    }
}