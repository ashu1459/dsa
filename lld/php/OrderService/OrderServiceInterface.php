<?php

interface OrderServiceInterface {

    /**
     * Update order status using Finite State Machine
     * 
     * @param int $orderId Order ID
     * @param string $status current status 
     * @param string $event Event requested
     * 
     * @return bool
     */
    public function changeState(int $orderId, string $status, string $event): bool;
}