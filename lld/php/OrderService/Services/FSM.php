<?php

namespace Services;

use Services\Status\StatusInterface;
use Services\Events\EventsInterface;

Class FSM implements FSMInterface {
    private int $order;
    private StatusInterface $status;
    private EventsInterface $events;
    private string $state;

    /**
     * @param int $order ID
     * @param StatusInterface $status
     * @param EventsInterface $event
     */
    public function __construct(
        $orderId, 
        StatusInterface $status, 
        EventsInterface $event
    ) {
        $this->order = $orderId;
        $this->status = $status;
        $this->events = $event;
        $this->setState();        
    }

    /**
     * @return void
     */
    private function setState() {
        $this->state = $this->status->get() . '_' . $this->events->get();
    }

    /**
     * @inherit
     */
    public function changeState(int $orderId, string $status, string $event): void {
        $this->order = $orderId;
        $this->status->set($status);
        $this->events->set($event);
        $this->setState();
    }

    /**
     * @return array
     */
    private function getOrderDetails(): array {
        # get random status
        $allStatuses = Status\StatusConstants::getAllStatuses();
        $randStatusKey = array_rand($allStatuses);
        
        # get random event
        $allEvents = Events\EventsConstants::getAllEvents();
        $randEventKey = array_rand($allEvents);

        # get random order ID
        $orderId = rand();

        return [
            'order_id' => $orderId,
            'status' => $this->status->getText($allStatuses[$randStatusKey]),
            'events' => $this->events->getText($allEvents[$randEventKey]),
        ];
    }
    
    /**
     * @inherit
     */
    public function getState(): string {
        # get state from DB and set here, then return
        $orderDetails = $this->getOrderDetails();
        
        $this->changeState(
            $orderDetails['order_id'], 
            $orderDetails['status'], 
            $orderDetails['events']
        );

        return $this->state;
    }
}